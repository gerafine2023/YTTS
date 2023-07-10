@echo off

echo Installing required Python libraries...
python -m pip install --upgrade pip
python -m pip install flask youtube_transcript_api

echo Starting local server...
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0 --port=3000

pause
