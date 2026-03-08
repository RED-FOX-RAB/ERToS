@echo off
REM ERToS Windows Test Runner
echo ERToS - Windows'ta test ediliyor...
echo.
echo Not: Bu araç Linux için tasarlanmıştır.
echo Windows'ta test etmek için Python ve PyQt5 gereklidir.
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo Python bulunamadı! Lütfen Python 3.8+ kurun.
    pause
    exit /b 1
)

echo Python bulundu. PyQt5 kontrol ediliyor...
python -c "import PyQt5" >nul 2>&1
if errorlevel 1 (
    echo PyQt5 bulunamadı. Kuruluyor...
    pip install PyQt5
)

echo.
echo ERToS başlatılıyor...
python main.py

pause
