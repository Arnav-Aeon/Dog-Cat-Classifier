@echo off
cd /d "%~dp0"

echo ======================================
echo Setting up environment...
echo ======================================

REM Create venv if it doesn't exist
if not exist venv (
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate

REM Install dependencies
pip install --upgrade pip
pip install -r script\requirements.txt

echo ======================================
echo Starting Streamlit App...
echo ======================================

streamlit run scripts\app.py

pause
