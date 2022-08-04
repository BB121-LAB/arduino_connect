@echo off
type ard_connect.py > ard_connect.pyw
pip3 install -r requirements.txt
pip3 install pyinstaller
pyinstaller --clean --onefile ard_connect.pyw
del /f /q ard_connect.pyw
