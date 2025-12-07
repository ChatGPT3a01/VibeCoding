@echo off
chcp 65001 >nul
echo ================================================
echo    AI 聊天助手 - 啟動程式
echo    作者：阿亮老師 (3A科技研究室)
echo ================================================
echo.

:: 檢查 .env 檔案是否存在
if not exist ".env" (
    echo [警告] 找不到 .env 檔案！
    echo.
    echo 請先複製 .env.example 為 .env 並填入你的 OpenAI API Key
    echo.
    copy .env.example .env
    echo 已為你建立 .env 檔案，請編輯它並填入 API Key
    echo.
    pause
    exit
)

:: 檢查虛擬環境是否存在
if exist "venv\Scripts\activate.bat" (
    echo [1/3] 啟動虛擬環境...
    call venv\Scripts\activate.bat
) else (
    echo [1/3] 建立虛擬環境...
    python -m venv venv
    call venv\Scripts\activate.bat

    echo [2/3] 安裝相依套件...
    pip install -r requirements.txt
)

echo [3/3] 啟動伺服器...
echo.
echo ================================================
echo 請開啟瀏覽器訪問: http://127.0.0.1:5000
echo 按 Ctrl+C 可停止伺服器
echo ================================================
echo.

python app.py

pause
