# 大葉大學 AI 工作坊

這個專案包含了一系列 AI 應用的實作範例，主要使用 LlamaIndex 和 OpenAI API 進行開發。

## 專案結構
```
.
├── 簡單RAG/                          # RAG (檢索增強生成) 實作範例
│   ├── RAG.ipynb                    # RAG 教學筆記本
│   ├── main.py                      # RAG 主程式
│   ├── test.py                      # 測試程式
│   ├── .env                         # 環境變數
│   ├── 大量文字/                    # 範例文件目錄
│   │   ├── TSMC 2Q24 Transcript.pdf # 台積電財報文件
│   │   └── TSMC 3Q24 Transcript.pdf # 台積電財報文件
│   ├── 帳單/                        # 帳單文件目錄
│   │   ├── Invoice-E22DD55C-0038.pdf
│   │   └── Invoice-E22DD55C-0039.pdf
│   ├── 議程/                        # 議程文件目錄
│   │   └── agenda.pdf              # 議程文件
│   ├── index_store_台積電資料/       # 台積電資料索引
│   ├── index_store_帳單/            # 帳單資料索引
│   └── index_store_議程/            # 議程資料索引
├── 簡單聊天機器人/                    # 基礎聊天機器人實作
│   ├── main.py                     # 主程式
│   ├── .env                        # 環境變數
│   └── data/                       # 資料目錄
│       └── 議程.pdf                 # 議程文件
├── 簡單聊天機器人網頁版/              # 網頁版聊天機器人
│   ├── main.py                     # 主程式
│   ├── .env                        # 環境變數
│   ├── .env.example                # 環境變數範例
│   ├── templates/                  # 網頁模板
│   │   └── index.html              # 主頁面
│   └── data/                       # 資料目錄
│       └── 2024NewFuturesFinal.pdf # 文件資料
├── 爬llamaindex文件/                # LlamaIndex 文件爬蟲
└── llamaindex_docs/                # LlamaIndex components教學文件
└── llamaindex_docs_module_guides/  # LlamaIndex modules教學文件

```

## 功能特色

1. **RAG 實作**
   - 支援多種文件格式 (PDF, TXT 等)
   - 文件內容向量化與檢索
   - 智慧問答功能
   - 多種索引儲存方式 (向量、圖形等)
   - 支援文件分塊與摘要生成

2. **聊天機器人**
   - 基礎版本：命令列介面
   - 網頁版本：使用 Flask 建置的網頁介面
   - 支援上下文對話
   - 整合 RAG 功能
   - 支援串流輸出

3. **文件爬蟲功能**
   - 自動爬取 LlamaIndex 官方文件
   - 支援 Markdown 格式轉換
   - 自動分類與整理文件
   - 支援增量更新
   - 保留文件結構

4. **LlamaIndex 功能**
   - 完整的模組使用教學
   - 多種檢索策略實作
   - 向量儲存與管理
   - 本地模型整合
   - 結構化輸出處理
   - 代理人系統整合
   - 自定義 LLM 和儲存
   - 元數擷取與管理
   - 文件處理管道
   - 查詢引擎優化
   - 可觀察性和評估
   - 工作流程自動化

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

## ���獻指南

歡迎提 Issue 或 Pull Request 來協助改善專案。

## 聯絡方式

如有任何問題，請透過 Issue 系統提出。