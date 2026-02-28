"""
RAG Agent Module

Modul ini berisi implementasi RAG (Retrieval-Augmented Generation) Agent yang menggunakan:
- ChromaDB sebagai vector database untuk retrieval
- Google Gemini sebagai LLM untuk generation
- LangChain tools untuk knowledge base retrieval dan Python code execution
- LangGraph untuk agent orchestration

Agent ini dapat:
1. Mencari informasi dari knowledge base berdasarkan query
2. Mengeksekusi kode Python untuk validasi
3. Mengingat konteks percakapan sebelumnya
"""

import os
import time
import re
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.tools import create_retriever_tool
from langchain_experimental.tools import PythonREPLTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

# Import untuk agent execution (LangChain 1.2+)
from langchain_classic.agents import AgentExecutor
from langchain.agents import create_agent


def load_vectordb():
    """
    Memuat ChromaDB vector database yang sudah dibuat oleh data_ingestion.py.
    
    Returns:
        Retriever: LangChain retriever untuk melakukan semantic search di ChromaDB
    """
    persist_dir = "./chroma_db_infotentor"
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    
    vectorstore = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )
    
    return vectorstore.as_retriever()


def setup_tools(retriever):
    """
    Setup tools untuk agent.
    
    Tools yang dibuat:
    1. Knowledge Base Tool: Untuk mencari dan mengambil materi dari ChromaDB
    2. Python Executor Tool: Untuk mengeksekusi kode Python secara real-time
    
    Args:
        retriever: LangChain retriever untuk ChromaDB
        
    Returns:
        list: List of tools yang siap digunakan oleh agent
    """
    # Tool 1: Knowledge Base Retriever
    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name="pencari_materi_informatika",
        description="Gunakan alat ini untuk mencari dan mengambil materi pembelajaran informatika, algoritma, dan pemrograman dari knowledge base. Gunakan ketika pengguna bertanya tentang teori, konsep, atau materi pembelajaran."
    )
    
    # Tool 2: Python Code Executor
    python_executor = PythonREPLTool(
        name="python_executor",
        description="Gunakan alat ini untuk mengeksekusi kode Python. Gunakan ketika pengguna meminta untuk menguji kode, menjalankan algoritma, atau memvalidasi bahwa kode berjalan tanpa error. Masukkan kode Python yang ingin dieksekusi."
    )
    
    return [retriever_tool, python_executor]


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """
    Mendapatkan atau membuat chat history untuk session tertentu.
    
    Implementasi menggunakan in-memory storage. Untuk production,
    pertimbangkan menggunakan persistent storage (database, Redis, dll).
    
    Args:
        session_id (str): Unique identifier untuk session
        
    Returns:
        BaseChatMessageHistory: Chat history untuk session tersebut
    """
    if not hasattr(get_session_history, "store"):
        get_session_history.store = {}
    
    if session_id not in get_session_history.store:
        get_session_history.store[session_id] = ChatMessageHistory()
    
    return get_session_history.store[session_id]


def create_rag_agent(api_key: str, session_id: str = "default"):
    """
    Membuat RAG Agent dengan semua komponen yang diperlukan.
    
    Args:
        api_key: Google Generative AI API Key
        session_id: ID untuk session chat (untuk memory)
    
    Returns:
        AgentExecutor yang siap digunakan
    """
    # 1. Load VectorDB
    print("Memuat VectorDB...")
    retriever = load_vectordb()
    
    # 2. Setup Tools
    print("Menyiapkan tools...")
    tools = setup_tools(retriever)
    
    # 3. Inisiasi LLM dengan fallback mechanism untuk model selection
    print("Menginisialisasi LLM (Gemini)...")
    # Prioritas: Flash models biasanya memiliki quota free tier yang lebih besar
    # Urutan model berdasarkan prioritas (ringan -> berat)
    model_names = [
        "gemini-flash-latest",      # Flash model - quota lebih besar, lebih cepat
        "gemini-2.0-flash",         # Flash model alternatif
        "gemini-2.5-flash",         # Flash model terbaru
        "gemini-pro-latest",        # Pro model (jika Flash tidak tersedia)
        "gemini-pro",               # Fallback ke model lama
    ]
    
    llm = None
    used_model = None
    
    for model_name in model_names:
        try:
            print(f"Mencoba model: {model_name}...")
            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=0.7
            )
            # Test dengan query sederhana untuk memastikan model bisa digunakan
            test_response = llm.invoke("Hello")
            used_model = model_name
            print(f"✓ Berhasil menggunakan model: {model_name}")
            break
        except ChatGoogleGenerativeAIError as e:
            error_str = str(e)
            # Jika error 429 (quota), coba model berikutnya
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print(f"✗ Model {model_name} quota habis, mencoba model berikutnya...")
                continue
            # Jika error 404 (model tidak ditemukan), coba model berikutnya
            elif "404" in error_str or "NOT_FOUND" in error_str:
                print(f"✗ Model {model_name} tidak ditemukan, mencoba model berikutnya...")
                continue
            else:
                # Error lain, tetap coba model berikutnya
                print(f"✗ Error dengan model {model_name}: {type(e).__name__}, mencoba model berikutnya...")
                continue
        except Exception as e:
            print(f"✗ Error tidak terduga dengan model {model_name}: {type(e).__name__}, mencoba model berikutnya...")
            continue
    
    if llm is None:
        raise ValueError(
            "❌ Tidak ada model Gemini yang dapat digunakan. "
            "Kemungkinan penyebab:\n"
            "1. Semua model telah mencapai batas quota free tier\n"
            "2. API Key tidak valid atau tidak memiliki akses\n"
            "3. Masalah koneksi ke Google API\n\n"
            "Solusi:\n"
            "- Tunggu beberapa saat dan coba lagi (quota biasanya reset setiap hari)\n"
            "- Periksa quota Anda di: https://ai.dev/rate-limit\n"
            "- Pastikan API Key valid di Google AI Studio"
        )
    
    # 4. System Prompt & Agent Configuration
    # System prompt mendefinisikan role dan behavior agent
    system_prompt = """Anda adalah Tutor Algoritma & Pemrograman yang cerdas dan ramah.

FORMAT OUTPUT (PENTING):
- Gunakan Markdown untuk formatting
- Gunakan heading (##, ###) untuk struktur yang jelas
- Gunakan bullet points (-) atau numbered lists (1., 2.) untuk list
- Gunakan code blocks dengan syntax highlighting untuk kode Python
- Gunakan inline code (`code`) untuk istilah teknis
- Jangan gunakan simbol Unicode yang aneh atau emoji berlebihan
- Gunakan spacing yang cukup antar paragraf

Instruksi penting:
1. **Untuk pertanyaan teori/konsep**: 
   - Gunakan alat "pencari_materi_informatika" untuk mencari dan mengambil materi yang relevan dari knowledge base sebelum menjawab
   - Struktur jawaban dengan jelas: Pengenalan → Penjelasan → Contoh (jika ada)

2. **Untuk permintaan kode/algoritma**: 
   - Tuliskan kode Python yang diminta dengan format yang rapi
   - Gunakan alat "python_executor" untuk mengeksekusi dan memvalidasi bahwa kode tersebut berjalan tanpa error
   - Setelah kode berhasil dieksekusi, tampilkan hasil eksekusi
   - Berikan penjelasan tentang bagaimana kode bekerja
   - Jika ada error, perbaiki kode dan coba lagi sampai berhasil

3. **Gaya komunikasi**: 
   - Ramah, profesional, dan mudah dipahami
   - Berikan penjelasan yang jelas dan terstruktur
   - Gunakan contoh konkret ketika menjelaskan konsep
   - Jika menggunakan materi dari knowledge base, sebutkan sumbernya
   - Hindari penggunaan simbol aneh atau karakter yang tidak perlu

4. **Ingat konteks percakapan**: Gunakan informasi dari percakapan sebelumnya untuk memberikan jawaban yang lebih relevan dan personal.

CONTOH FORMAT OUTPUT YANG BAIK:

## Pengenalan Algoritma Pencarian

Algoritma pencarian adalah metode untuk menemukan data tertentu dalam kumpulan data.

### 1. Linear Search

Linear Search adalah algoritma pencarian paling sederhana.

**Cara kerja:**
- Memeriksa setiap elemen dari awal hingga akhir
- Berhenti ketika data ditemukan atau semua data telah diperiksa

**Contoh kode:**
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Kompleksitas:** O(n)
"""
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # 5. Buat Agent menggunakan LangGraph
    # Bind tools ke LLM untuk enable function calling
    llm_with_tools = llm.bind_tools(tools)
    
    # Buat agent graph menggunakan create_agent (LangGraph approach)
    # create_agent mengembalikan CompiledStateGraph yang bisa di-invoke langsung
    agent_graph = create_agent(
        model=llm_with_tools,
        tools=tools,
        system_prompt=system_prompt
    )
    
    # Agent graph siap digunakan (LangGraph graph bisa di-invoke langsung)
    agent_executor = agent_graph
    
    # 6. Wrapper function untuk menjalankan agent dengan memory dan retry logic
    def run_with_memory(user_input: str, max_retries: int = 3):
        """
        Menjalankan agent dengan chat history dan retry logic untuk error handling.
        
        Args:
            user_input (str): Input dari pengguna
            max_retries (int): Maksimal jumlah retry untuk error 429 (quota)
            
        Returns:
            dict: Dictionary dengan key 'output' berisi response dari agent
        """
        # Ambil chat history untuk session ini (fresh setiap kali)
        message_history = get_session_history(session_id)
        
        # Tambahkan user message ke history
        message_history.add_user_message(user_input)
        
        # Ambil chat history terbaru
        chat_history = message_history.messages
        
        # Jalankan agent dengan chat history
        # LangGraph menggunakan format yang berbeda
        # Kita perlu mengkonversi chat_history ke format yang sesuai
        from langchain_core.messages import HumanMessage, AIMessage
        
        # Konversi chat_history ke format messages
        messages = []
        for msg in chat_history:
            if hasattr(msg, 'content'):
                messages.append(msg)
            else:
                # Jika format berbeda, konversi
                if msg.type == "human":
                    messages.append(HumanMessage(content=msg.content))
                elif msg.type == "ai":
                    messages.append(AIMessage(content=msg.content))
        
        # Tambahkan user input terbaru
        messages.append(HumanMessage(content=user_input))
        
        # Retry logic untuk 429 errors
        last_exception = None
        for attempt in range(max_retries):
            try:
                # Invoke agent graph
                result_dict = agent_executor.invoke({"messages": messages})
                
                # Ekstrak output dari result
                if isinstance(result_dict, dict):
                    if "messages" in result_dict:
                        # Ambil message terakhir (AI response)
                        last_message = result_dict["messages"][-1]
                        
                        # Handle list of contents (seperti text blocks dan tool calls)
                        if isinstance(last_message.content, list):
                            text_parts = []
                            for part in last_message.content:
                                if isinstance(part, str):
                                    text_parts.append(part)
                                elif isinstance(part, dict) and "text" in part:
                                    text_parts.append(part["text"])
                            output = "\n".join(text_parts)
                        else:
                            # Jika hanya string atau object lain yang punya atribut content
                            output = str(last_message.content) if hasattr(last_message, 'content') else str(last_message)
                    else:
                        output = str(result_dict.get("output", str(result_dict)))
                else:
                    output = str(result_dict)
                
                result = {"output": output}
                
                # Tambahkan AI response ke history
                message_history.add_ai_message(result["output"])
                
                return result
                
            except ChatGoogleGenerativeAIError as e:
                error_str = str(e)
                last_exception = e
                
                # Jika error 429 (quota), tunggu dan retry
                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    # Extract retry delay dari error message jika ada
                    retry_delay = 10  # Default 10 detik
                    if "retry in" in error_str.lower() or "retryDelay" in error_str:
                        try:
                            # Coba extract angka dari pesan error
                            import re
                            delay_match = re.search(r'retry in ([\d.]+)', error_str, re.IGNORECASE)
                            if delay_match:
                                retry_delay = max(5, int(float(delay_match.group(1))) + 2)  # Tambah 2 detik buffer
                        except:
                            pass
                    
                    if attempt < max_retries - 1:
                        wait_time = retry_delay * (attempt + 1)  # Exponential backoff
                        print(f"⚠️ Quota habis. Menunggu {wait_time} detik sebelum retry (attempt {attempt + 1}/{max_retries})...")
                        time.sleep(wait_time)
                        continue
                    else:
                        # Semua retry gagal
                        raise ValueError(
                            f"❌ Quota API habis setelah {max_retries} percobaan.\n\n"
                            f"Detail error: {error_str}\n\n"
                            f"Solusi:\n"
                            f"- Tunggu beberapa saat (quota biasanya reset setiap hari)\n"
                            f"- Periksa quota Anda di: https://ai.dev/rate-limit\n"
                            f"- Model yang digunakan: {used_model or 'tidak diketahui'}\n"
                            f"- Coba lagi nanti atau upgrade ke paid plan"
                        ) from e
                else:
                    # Error lain, langsung raise
                    raise
                    
            except Exception as e:
                # Error tidak terduga, langsung raise
                raise
        
        # Jika semua retry gagal dan tidak ada exception yang di-raise
        if last_exception:
            raise last_exception
        else:
            raise RuntimeError("Gagal menjalankan agent setelah beberapa percobaan")
    
    return run_with_memory, agent_executor


if __name__ == "__main__":
    # Contoh penggunaan
    import sys
    
    # Ambil API key dari environment variable atau secrets
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY tidak ditemukan di environment variable.")
        print("Set GOOGLE_API_KEY terlebih dahulu atau gunakan dari Streamlit secrets.")
        sys.exit(1)
    
    # Buat agent
    run_agent, executor = create_rag_agent(api_key, session_id="test_session")
    
    print("\n" + "="*50)
    print("RAG Agent siap digunakan!")
    print("="*50 + "\n")
    
    # Test query
    test_query = "Apa itu algoritma?"
    print(f"Test Query: {test_query}\n")
    result = run_agent(test_query)
    print(f"\nResponse: {result['output']}")
