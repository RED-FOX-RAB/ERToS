#!/bin/bash
# ERToS Hızlı Kurulum Script'i

echo "======================================"
echo "  ERToS Kurulum Başlatılıyor..."
echo "======================================"

# Root kontrolü
if [ "$EUID" -eq 0 ]; then 
    echo "Bu script'i root olarak çalıştırmayın!"
    exit 1
fi

# Arch Linux kontrolü
if [ ! -f /etc/arch-release ]; then
    echo "Uyarı: Bu script Arch Linux için optimize edilmiştir."
    read -p "Devam etmek istiyor musunuz? (e/h): " choice
    if [ "$choice" != "e" ]; then
        exit 0
    fi
fi

# Python kontrolü
if ! command -v python3 &> /dev/null; then
    echo "Python3 kurulu değil. Kuruluyor..."
    sudo pacman -S --noconfirm python python-pip
fi

# PyQt5 kurulumu
echo "PyQt5 kuruluyor..."
pip install --user PyQt5

# Wine kontrolü
if ! command -v wine &> /dev/null; then
    echo "Wine kurulu değil."
    read -p "Wine'ı şimdi kurmak ister misiniz? (e/h): " wine_choice
    if [ "$wine_choice" = "e" ]; then
        sudo pacman -S --noconfirm wine winetricks
    fi
fi

# Desktop entry oluştur
echo "Desktop kısayolu oluşturuluyor..."
mkdir -p ~/.local/share/applications

cat > ~/.local/share/applications/ertos.desktop << EOF
[Desktop Entry]
Type=Application
Name=ERToS
Comment=EXE Runner Tool on System
Exec=python3 $(pwd)/main.py
Icon=$(pwd)/icon.svg
Categories=Utility;System;
Terminal=false
EOF

# İkon oluştur
cat > icon.svg << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<svg width="256" height="256" xmlns="http://www.w3.org/2000/svg">
  <rect width="256" height="256" fill="#2196F3" rx="20"/>
  <text x="128" y="140" font-family="Arial" font-size="80" fill="white" text-anchor="middle" font-weight="bold">EXE</text>
  <text x="128" y="200" font-family="Arial" font-size="40" fill="white" text-anchor="middle">Runner</text>
</svg>
EOF

# Çalıştırılabilir yap
chmod +x main.py

echo ""
echo "======================================"
echo "  Kurulum Tamamlandı!"
echo "======================================"
echo ""
echo "ERToS'u çalıştırmak için:"
echo "  1. Uygulama menüsünden 'ERToS' arayın"
echo "  2. Veya terminal'den: python3 $(pwd)/main.py"
echo ""
echo "AppImage oluşturmak için:"
echo "  ./build-appimage.sh"
echo ""
