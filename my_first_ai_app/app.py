# app.py - AI 聊天助手後端程式
# 作者：曾慶良 (阿亮老師) - 3A科技研究室
# 版本：2.0.0 - 支援 OpenAI 和 Google Gemini

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

# 建立 Flask 應用
app = Flask(__name__)

# 取得 AI 提供者設定
AI_PROVIDER = os.getenv('AI_PROVIDER', 'openai').lower()

# 初始化 AI 客戶端
if AI_PROVIDER == 'google':
    import google.generativeai as genai
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("使用 Google Gemini API")
else:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    print("使用 OpenAI API")

# 首頁路由
@app.route('/')
def index():
    return render_template('index.html', ai_provider=AI_PROVIDER)

# 聊天 API 路由
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # 取得使用者訊息
        user_message = request.json.get('message')

        if not user_message:
            return jsonify({"error": "請輸入訊息"}), 400

        # 根據設定使用不同的 AI 服務
        if AI_PROVIDER == 'google':
            # 使用 Google Gemini
            response = model.generate_content(
                f"你是一個友善的 AI 助手，請用繁體中文回答。\n\n使用者問題：{user_message}"
            )
            ai_response = response.text
        else:
            # 使用 OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是一個友善的 AI 助手，請用繁體中文回答。"},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            ai_response = response.choices[0].message.content

        return jsonify({"response": ai_response})

    except Exception as e:
        print(f"錯誤: {str(e)}")
        return jsonify({"error": f"發生錯誤: {str(e)}"}), 500

# 啟動伺服器
if __name__ == '__main__':
    print("=" * 50)
    print("AI 聊天助手已啟動！")
    print(f"AI 提供者: {'Google Gemini' if AI_PROVIDER == 'google' else 'OpenAI'}")
    print("請開啟瀏覽器訪問: http://127.0.0.1:5000")
    print("按 Ctrl+C 停止伺服器")
    print("=" * 50)
    app.run(debug=True, port=5000)
