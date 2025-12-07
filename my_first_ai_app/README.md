# AI 聊天助手

這是《零基礎到大師》書籍 CH0 的實作範例 - 你的第一個 AI 應用程式。

## 功能特色

- 支援 **OpenAI GPT** 和 **Google Gemini** 雙 API（二選一）
- 現代化的聊天介面
- 即時回應與載入動畫
- 錯誤處理機制
- 繁體中文介面

## 快速開始

### Windows 使用者

1. 複製 `.env.example` 為 `.env`
2. 編輯 `.env` 檔案：
   - 填入你的 API Key（OpenAI 或 Google 二選一）
   - 設定 `AI_PROVIDER=openai` 或 `AI_PROVIDER=google`
3. 雙擊執行 `啟動.bat`
4. 開啟瀏覽器訪問 http://127.0.0.1:5000

### 手動安裝

```bash
# 1. 建立虛擬環境
python -m venv venv

# 2. 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. 安裝套件
pip install -r requirements.txt

# 4. 設定環境變數
copy .env.example .env
# 編輯 .env 填入你的 API Key

# 5. 啟動應用
python app.py
```

## 取得 API Key

### OpenAI API Key
1. 前往 https://platform.openai.com/api-keys
2. 登入或註冊帳號
3. 點擊「Create new secret key」
4. 複製 API Key 貼到 `.env` 檔案中

### Google Gemini API Key
1. 前往 https://aistudio.google.com/app/apikey
2. 登入 Google 帳號
3. 點擊「Create API Key」
4. 複製 API Key 貼到 `.env` 檔案中

## 專案結構

```
my_first_ai_app/
├── app.py              # Flask 後端程式（支援雙 API）
├── requirements.txt    # Python 套件清單
├── .env.example        # 環境變數範例
├── .env                # 環境變數（需自行建立）
├── .gitignore          # Git 忽略檔案
├── 啟動.bat            # Windows 快速啟動
├── README.md           # 本文件
└── templates/
    └── index.html      # 前端網頁
```

## 作者

曾慶良 (阿亮老師) - 3A科技研究室

---

**Keep Vibing, Keep Coding!**
