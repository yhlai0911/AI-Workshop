import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Document, Settings
from llama_index.llms.openai import OpenAI
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

# 載入環境變數
load_dotenv()

# 設定OpenAI API金鑰
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '簡單聊天機器人網頁版/data'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB 最大上傳限制

# 確保上傳目錄存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class ChatBot:
    def __init__(self, model="gpt-4o-mini", temperature=0.7):
        """初始化聊天機器人"""
        self.index = None
        self.query_engine = None
        Settings.llm = OpenAI(model=model, temperature=temperature)
        
    def load_data(self, directory):
        """從指定目錄載入文件資料"""
        try:
            documents = SimpleDirectoryReader(directory).load_data()
            self.index = VectorStoreIndex.from_documents(documents)
            self.query_engine = self.index.as_query_engine()
            return True
        except Exception as e:
            print(f"載入資料時發生錯誤: {str(e)}")
            return False
            
    def chat(self, message: str) -> str:
        """處理使用者輸入並回傳回應"""
        try:
            if not self.query_engine:
                return "請先上傳檔案!"
            response = self.query_engine.query(message)
            return str(response)
        except Exception as e:
            return f"發生錯誤: {str(e)}"

# 全域變數儲存聊天機器人實例
bot = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global bot
    
    # 獲取 LLM 參數
    model = request.form.get('model', 'gpt-4o-mini')
    temperature = float(request.form.get('temperature', 0.7))
    
    # 初始化新的聊天機器人
    bot = ChatBot(model=model, temperature=temperature)
    
    if 'file' not in request.files:
        return jsonify({'error': '沒有上傳檔案'}), 400
        
    files = request.files.getlist('file')
    
    # 清空上傳目錄
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))
    
    # 保存所有上傳的檔案
    for file in files:
        if file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    # 載入檔案
    if bot.load_data(app.config['UPLOAD_FOLDER']):
        return jsonify({'message': '檔案上傳成功！'}), 200
    else:
        return jsonify({'error': '檔案處理失敗'}), 500

@app.route('/chat', methods=['POST'])
def chat():
    global bot
    if not bot:
        return jsonify({'error': '請先上傳檔案並設定參數'}), 400
        
    message = request.json.get('message')
    if not message:
        return jsonify({'error': '請輸入訊息'}), 400
        
    response = bot.chat(message)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
