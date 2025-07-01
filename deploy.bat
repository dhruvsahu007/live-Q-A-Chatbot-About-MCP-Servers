@echo off
echo 🚀 Preparing MCP Q&A Chatbot for Render deployment...

REM Check if git is initialized
if not exist ".git" (
    echo 📝 Initializing Git repository...
    git init
)

REM Add all files
echo 📦 Adding files to Git...
git add .

REM Commit changes
echo 💾 Committing changes...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Deploy MCP Q&A Chatbot to Render
git commit -m "%commit_msg%"

REM Check if remote origin exists
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo 🔗 Add your GitHub repository URL:
    set /p repo_url="Enter GitHub repo URL (https://github.com/username/repo.git): "
    git remote add origin "%repo_url%"
)

REM Push to GitHub
echo ⬆️ Pushing to GitHub...
git branch -M main
git push -u origin main

echo ✅ Code pushed to GitHub!
echo.
echo 📋 Next steps:
echo 1. Go to https://render.com
echo 2. Sign in with your GitHub account
echo 3. Create a new Web Service
echo 4. Connect your GitHub repository
echo 5. Set these environment variables in Render:
echo    - OPENAI_API_KEY=your_api_key_here
echo    - OPENAI_MODEL=gpt-3.5-turbo
echo    - MAX_TOKENS=1000
echo    - TEMPERATURE=0.7
echo 6. Deploy!
echo.
echo 📖 For detailed instructions, see DEPLOYMENT.md

pause
