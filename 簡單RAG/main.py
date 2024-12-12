#pip install llama-index

import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.llms.openai import OpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.7)

# 載入資料
documents = SimpleDirectoryReader("/Users/apple/Dropbox/AI工作坊/簡單RAG/data").load_data()
# 建立向量索引
index = VectorStoreIndex.from_documents(documents)

# 建立聊天記憶體
memory = ChatMemoryBuffer.from_defaults(token_limit=1500)

# 建立聊天引擎
chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt="你是一個友善的助手，會基於提供的文件來回答問題。如果問題超出文件範圍，請誠實告知。"
)

# 開始聊天循環
print("開始聊天！(輸入 'quit' 結束對話)")
while True:
    user_input = input("你: ")
    if user_input.lower() == 'quit':
        break
        
    # 獲取回應
    response = chat_engine.chat(user_input)
    print("助手:", response.response)
