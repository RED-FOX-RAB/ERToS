#!/bin/bash
# ERToS AppImage Build Script

set -e

echo "ERToS AppImage oluşturuluyor..."

# Gerekli araçları kontrol et
if ! command -v python3 &> /dev/null; then
    echo "Python3 bulunamadı!"
    exit 1
fi

# AppImage araçlarını indir
if [ ! -f "appimagetool-x86_64.AppImage" ]; then
    echo "appimagetool indiriliyor..."
    wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
    chmod +x appimagetool-x86_64.AppImage
fi

# AppDir oluştur
echo "AppDir yapısı oluşturuluyor..."
rm -rf ERToS.AppDir
mkdir -p ERToS.AppDir/usr/bin
mkdir -p ERToS.AppDir/usr/lib
mkdir -p ERToS.AppDir/usr/share/applications
mkdir -p ERToS.AppDir/usr/share/icons/hicolor/256x256/apps

# Python ve bağımlılıkları kopyala
echo "Python bağımlılıkları hazırlanıyor..."
pip3 install --target=ERToS.AppDir/usr/lib PyQt5

# Ana script'i kopyala
cp main.py ERToS.AppDir/usr/bin/ertos
chmod +x ERToS.AppDir/usr/bin/ertos

# AppRun oluştur
cat > ERToS.AppDir/AppRun << 'EOF'
#!/bin/bash
SELF=$(readlink -f "$0")
HERE=${SELF%/*}
export PATH="${HERE}/usr/bin:${PATH}"
export LD_LIBRARY_PATH="${HERE}/usr/lib:${LD_LIBRARY_PATH}"
export PYTHONPATH="${HERE}/usr/lib:${PYTHONPATH}"
export PYTHONHOME="${HERE}/usr"
exec python3 "${HERE}/usr/bin/ertos" "$@"
EOF
chmod +x ERToS.AppDir/AppRun

# Desktop dosyası oluştur
cat > ERToS.AppDir/ertos.desktop << EOF
[Desktop Entry]
Type=Application
Name=ERToS
Comment=EXE Runner Tool on System
Exec=ertos
Icon=ertos
Categories=Utility;System;
Terminal=false
EOF

cp ERToS.AppDir/ertos.desktop ERToS.AppDir/usr/share/applications/

# İkon oluştur (basit bir SVG)
cat > ERToS.AppDir/ertos.svg << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<svg width="256" height="256" xmlns="http://www.w3.org/2000/svg">
  <rect width="256" height="256" fill="#2196F3" rx="20"/>
  <text x="128" y="140" font-family="Arial" font-size="80" fill="white" text-anchor="middle" font-weight="bold">EXE</text>
  <text x="128" y="200" font-family="Arial" font-size="40" fill="white" text-anchor="middle">Runner</text>
</svg>
EOF

cp ERToS.AppDir/ertos.svg ERToS.AppDir/usr/share/icons/hicolor/256x256/apps/
ln -sf usr/share/icons/hicolor/256x256/apps/ertos.svg ERToS.AppDir/ertos.svg

# AppImage oluştur
echo "AppImage paketleniyor..."
./appimagetool-x86_64.AppImage ERToS.AppDir ERToS-x86_64.AppImage

echo "Başarılı! ERToS-x86_64.AppImage oluşturuldu."
echo "Çalıştırmak için: ./ERToS-x86_64.AppImage"
