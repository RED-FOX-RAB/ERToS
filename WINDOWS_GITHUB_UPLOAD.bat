@echo off
echo ========================================
echo   ERToS GitHub Yukleme Script'i
echo ========================================
echo.

REM Git kontrolu
git --version >nul 2>&1
if errorlevel 1 (
    echo Git bulunamadi!
    echo Lutfen Git'i yukleyin: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo Git bulundu!
echo.

REM Kullanici bilgileri
set /p USERNAME="GitHub kullanici adiniz: "
set /p EMAIL="GitHub email adresiniz: "

echo.
echo Git yapilandiriliyor...
git config --global user.name "%USERNAME%"
git config --global user.email "%EMAIL%"

echo.
echo Git repository baslatiliyor...
git init

echo.
echo Dosyalar ekleniyor...
git add .

echo.
echo Commit yapiliyor...
git commit -m "feat: ERToS v1.0 - Modern GUI ile Windows .exe runner"

echo.
echo GitHub repository URL'inizi girin (ornek: https://github.com/kullaniciadi/ERToS.git)
set /p REPO_URL="Repository URL: "

echo.
echo Remote ekleniyor...
git remote add origin %REPO_URL%

echo.
echo Ana branch ayarlaniyor...
git branch -M main

echo.
echo GitHub'a yukleniyor...
echo Not: Sifre yerine GitHub Personal Access Token kullanmaniz gerekebilir!
echo Token olusturmak icin: https://github.com/settings/tokens
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo HATA: Yukleme basarisiz!
    echo.
    echo Cozum 1: GitHub Personal Access Token kullanin
    echo   1. https://github.com/settings/tokens adresine gidin
    echo   2. "Generate new token (classic)" tiklayin
    echo   3. "repo" yetkilerini secin
    echo   4. Token'i kopyalayin
    echo   5. Sifre yerine token'i kullanin
    echo.
    echo Cozum 2: SSH kullanin
    echo   ssh-keygen -t ed25519 -C "%EMAIL%"
    echo   Public key'i GitHub'a ekleyin
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   BASARILI! Proje GitHub'a yuklendi!
echo ========================================
echo.
echo Projeniz: %REPO_URL%
echo.
pause
