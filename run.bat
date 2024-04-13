pytest -s -v testCases/excel.py

rem pytest -s -v testCases/test_login.py

@echo off
echo Running Selenium tests...

rem Activate virtual environment (if applicable)
call venv\Scripts\activate

rem Navigate to the directory containing your Python script
cd C:\auto\april\testCases

rem Run the Python script
python excel.py

rem Deactivate virtual environment (if applicable)
deactivate