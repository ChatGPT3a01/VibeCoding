# CH0 | Vibe Coding 氛圍編程

> 與 AI 協作開發的新時代 - 用自然語言描述需求，讓 AI 幫你實現想法

---

## 課程簡報

**[點擊這裡查看完整課程簡報](https://chatgpt3a01.github.io/VibeCoding/簡報/index.html)**

### 單元列表

| Part | 主題 | 內容重點 |
|------|------|----------|
| [Part 1](https://chatgpt3a01.github.io/VibeCoding/簡報/Part1_認識VibeCoding.html) | 認識 Vibe Coding | 什麼是 Vibe Coding、為什麼重要、應用案例 |
| [Part 2](https://chatgpt3a01.github.io/VibeCoding/簡報/Part2_提示詞的藝術.html) | 提示詞的藝術 | 核心原則、好的提示詞範例、進階技巧 |
| [Part 3](https://chatgpt3a01.github.io/VibeCoding/簡報/Part3_實用工具.html) | 實用工具 | Vibe Coding 捕夢網、OpenAI Playground |
| [Part 4](https://chatgpt3a01.github.io/VibeCoding/簡報/Part4_技術與實作.html) | 技術與實作 | 前後端架構、程式碼展示、實作 Demo |
| [Part 5](https://chatgpt3a01.github.io/VibeCoding/簡報/Part5_總結與展望.html) | 總結與展望 | 核心概念回顧、學習建議 |

---

## 實作專案：AI 聊天助手

本章節包含一個完整的 AI 聊天助手專案，支援 **OpenAI GPT** 和 **Google Gemini** 雙 API。

### 專案結構

```
VibeCoding/
├── README.md                 # 本文件
├── my_first_ai_app/          # AI 聊天助手專案
│   ├── app.py                # Flask 後端程式
│   ├── requirements.txt      # Python 套件清單
│   ├── .env.example          # 環境變數範例
│   ├── .gitignore            # Git 忽略檔案
│   ├── 啟動.bat              # Windows 快速啟動
│   └── templates/
│       └── index.html        # 前端網頁
├── 簡報/                     # 課程簡報 HTML
└── 截圖/                     # 教學截圖
```

---

## 快速開始

### 方法一：下載專案

```bash
# 克隆專案
git clone https://github.com/ChatGPT3a01/VibeCoding.git

# 進入專案目錄
cd VibeCoding/my_first_ai_app
```

或直接[下載 ZIP](https://github.com/ChatGPT3a01/VibeCoding/archive/refs/heads/main.zip)

### 方法二：Windows 快速啟動

1. 下載專案後，進入 `my_first_ai_app` 資料夾
2. 複製 `.env.example` 為 `.env`
3. 編輯 `.env` 填入你的 API Key（OpenAI 或 Google 二選一）
4. 雙擊執行 `啟動.bat`
5. 開啟瀏覽器訪問 http://127.0.0.1:5000

### 方法三：手動安裝

```bash
# 1. 進入專案目錄
cd my_first_ai_app

# 2. 建立虛擬環境
python -m venv venv

# 3. 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. 安裝套件
pip install -r requirements.txt

# 5. 設定環境變數
copy .env.example .env   # Windows
cp .env.example .env     # macOS/Linux

# 6. 編輯 .env 填入你的 API Key

# 7. 啟動應用
python app.py
```

---

## 環境變數設定

編輯 `.env` 檔案，選擇使用 OpenAI 或 Google Gemini（二選一）：

```env
# 選項 1: OpenAI API Key
OPENAI_API_KEY=sk-你的API金鑰

# 選項 2: Google Gemini API Key
GOOGLE_API_KEY=AIza你的API金鑰

# 選擇 AI 提供者 (openai 或 google)
AI_PROVIDER=openai
```

### 取得 API Key

| 平台 | 取得方式 |
|------|----------|
| OpenAI | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| Google Gemini | [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) |

---

## 技術架構

### 前端技術
- **HTML5** - 網頁結構
- **CSS3** - 樣式設計（漸層背景、響應式設計）
- **JavaScript (ES6+)** - 非同步請求、DOM 操作

### 後端技術
- **Python 3.8+** - 主要程式語言
- **Flask** - Web 框架
- **python-dotenv** - 環境變數管理

### AI 服務
- **OpenAI GPT-3.5-turbo** - 文字生成
- **Google Gemini 1.5 Flash** - 文字生成

### 開發工具建議
- **VS Code** - 程式碼編輯器
- **Claude Code CLI** - AI 輔助開發
- **Git** - 版本控制

---

## 相關資源

### 課程工具
- **[Vibe Coding 捕夢網](https://vibe-coding-gem.netlify.app/)** - 提示詞生成工具
- **[捕夢網原始碼](https://github.com/ChatGPT3a01/Vibe_Coding_DreamCatcher)** - GitHub 專案
- **[OpenAI Playground](https://platform.openai.com/playground)** - 提示詞測試平台

### 學習資源
- [OpenAI API 文件](https://platform.openai.com/docs)
- [Google AI Studio](https://aistudio.google.com/)
- [Flask 官方文件](https://flask.palletsprojects.com/)

---

## 常見問題

### Q: API Key 從哪裡取得？
A: OpenAI 請到 [platform.openai.com](https://platform.openai.com/api-keys)，Google Gemini 請到 [aistudio.google.com](https://aistudio.google.com/app/apikey)

### Q: 出現 "ModuleNotFoundError" 錯誤？
A: 確認已啟動虛擬環境並執行 `pip install -r requirements.txt`

### Q: 出現 "API Key 無效" 錯誤？
A: 檢查 `.env` 檔案中的 API Key 是否正確，以及 `AI_PROVIDER` 設定是否與你的 API Key 對應

### Q: Port 5000 被佔用？
A: 修改 `app.py` 最後一行的 `port=5000` 為其他數字（如 5001）

---

## 作者

**曾慶良 (阿亮老師)** - 3A科技研究室

- [Facebook](https://www.facebook.com/yt3a01)
- [YouTube](https://www.youtube.com/@3aLearn)

---

## 授權

本專案為《自己架設 AI - 零基礎到大師》書籍配套教材，供學習使用。

---

**Keep Vibing, Keep Coding!**
