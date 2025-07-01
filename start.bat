@echo off
echo ========================================
echo    MCP Q&A Chatbot - Quick Start
echo ========================================
echo.

REM Check if virtual environment is activated
if "%VIRTUAL_ENV%"=="" (
    echo Warning: No virtual environment detected
    echo It's recommended to use a virtual environment
    echo.
    pause
)

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements
    pause
    exit /b 1
)

REM Check if .env exists
if not exist ".env" (
    if exist ".env.example" (
        echo Creating .env file from template...
        copy ".env.example" ".env"
        echo.
        echo *** IMPORTANT ***
        echo Please edit .env file and add your OpenAI API key
        echo Press any key to open .env file...
        pause
        notepad .env
    ) else (
        echo .env.example not found!
        pause
        exit /b 1
    )
)

REM Run setup test
echo.
echo Running setup test...
python setup.py --test
if %errorlevel% neq 0 (
    echo Setup test failed. Please fix the issues above.
    pause
    exit /b 1
)

REM Start the application
echo.
echo Starting MCP Q&A Chatbot...
echo The application will open in your default browser
echo Press Ctrl+C to stop the application
echo.
streamlit run app.py

pause
