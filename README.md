# AI 工作坊

這個專案包含了一系列 AI 應用的實作範例，主要使用 LlamaIndex 和 OpenAI API 進行開發。

## 專案結構
```
.
├── 簡單RAG/                    # RAG (檢索增強生成) 實作範例
│   ├── RAG.ipynb              # RAG 教學筆記本
│   ├── 大量文字/              # 範例文件
│   ├── index_store_台積電資料/  # 台積電資料索引
│   └── index_store_帳單/      # 帳單資料索引
├── 簡單聊天機器人/             # 基礎聊天機器人實作
│   ├── main.py               # 主程式
│   └── data/                 # 資料目錄
└── 簡單聊天機器人網頁版/        # 網頁版聊天機器人
    ├── main.py               # 主程式
    ├── templates/            # 網頁模板
    └── data/                 # 資料目錄
```

## 功能特色

1. **RAG 實作**
   - 支援多種文件格式 (PDF, TXT 等)
   - 文件內容向量化與檢索
   - 智慧問答功能

2. **聊天機器人**
   - 基礎版本：命令列介面
   - 網頁版本：使用 Flask 建置的網頁介面
   - 支援上下文對話

## 環境設定

### 前置需求
- Python 3.8+
- pip 套件管理工具

### 安裝步驟

1. 複製專案
   ```bash
   git clone https://github.com/your-username/AI-Workshop.git
   cd AI-Workshop
   ```

2. 安裝相依套件
   ```bash
   pip install -r requirements.txt
   ```

3. 環境變數設定
   - 複製 `.env.example` 到 `.env`
   - 在 `.env` 中填入您的 OpenAI API Key

### 使用方式

1. **RAG 系統**
   ```bash
   cd 簡單RAG
   jupyter notebook RAG.ipynb
   ```

2. **基礎聊天機器人**
   ```bash
   cd 簡單聊天機器人
   python main.py
   ```

3. **網頁版聊天機器人**
   ```bash
   cd 簡單聊天機器人網頁版
   python main.py
   ```
   然後在瀏覽器開啟 `http://localhost:5000`

## 注意事項

- 請確保您有足夠的 OpenAI API 額度
- 大型文件處理可能需要較長時間
- 建議使用虛擬環境進行開發

## 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

## 貢獻指南

歡迎提交 Issue 或 Pull Request 來協助改善專案。

## 聯絡方式

如有任何問題，請透過 Issue 系統提出。