import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document, Settings
from llama_index.llms.openai import OpenAI

# 載入環境變數
load_dotenv()

# 設定OpenAI API金鑰
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 初始化LLM
Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.7)

class ChatBot:
    def __init__(self):
        """初始化聊天機器人"""
        self.index = None
        self.query_engine = None
        
    def load_data(self, directory="簡單聊天機器人/data"):
        """從指定目錄載入文件資料"""
        try:
            # 使用SimpleDirectoryReader載入文件
            documents = SimpleDirectoryReader(directory).load_data()
            
            # 建立向量索引
            self.index = VectorStoreIndex.from_documents(documents)
            
            # 建立查詢引擎
            self.query_engine = self.index.as_query_engine()
            
            print("資料載入成功!")
            return True
            
        except Exception as e:
            print(f"載入資料時發生錯誤: {str(e)}")
            return False
            
    def chat(self, message: str) -> str:
        """處理使用者輸入並回傳回應"""
        try:
            if not self.query_engine:
                return "請先載入資料!"
                
            # 使用query_engine查詢回應
            response = self.query_engine.query(message)
            return str(response)
            
        except Exception as e:
            return f"發生錯誤: {str(e)}"

def main():
    # 初始化聊天機器人
    bot = ChatBot()
    
    # 載入資料
    if not bot.load_data():
        print("無法啟動聊天機器人,請確認資料目錄是否存在")
        return
        
    print("聊天機器人已啟動! 輸入 'exit' 結束對話")
    
    # 開始對話迴圈
    while True:
        user_input = input("你: ")
        
        if user_input.lower() == 'exit':
            print("再見!")
            break
            
        response = bot.chat(user_input)
        print(f"機器人: {response}")

if __name__ == "__main__":
    main()
