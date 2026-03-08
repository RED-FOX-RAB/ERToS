# ERToS - EXE Runner Tool on System

<div align="center">

![ERToS Logo](https://img.shields.io/badge/ERToS-v1.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux-orange?style=for-the-badge&logo=linux)

**Windows .exe dosyalarını Linux'ta çalıştırmak için modern GUI tabanlı araç**

[Özellikler](#özellikler) • [Kurulum](#kurulum) • [Kullanım](#kullanım) • [Ekran Görüntüleri](#ekran-görüntüleri) • [Katkıda Bulunma](#katkıda-bulunma)

</div>

---

## ✨ Özellikler

- 🚀 **Otomatik Wine Kurulumu** - İlk çalıştırmada Wine otomatik kurulur
- 🎨 **Modern PyQt5 GUI** - Renkli ve kullanıcı dostu arayüz
- 📦 **AppImage Formatı** - Portable, kurulum gerektirmez
- ⚙️ **Wine Yapılandırma** - Winecfg ve Winetricks desteği
- 🔧 **Arch Linux Optimize** - Arch Linux için özel optimize edilmiş
- 🌈 **Gradient Tasarım** - Modern ve şık görünüm
- 📋 **Gerçek Zamanlı Çıktı** - Program çıktısını canlı görüntüleme

## 📸 Ekran Görüntüleri

```
┌─────────────────────────────────────────┐
│           ERToS v1.0                    │
│  🚀 Windows .exe'leri Linux'ta çalıştır │
├─────────────────────────────────────────┤
│  🏠 Ana  │  ⚙️ Ayarlar  │  ℹ️ Hakkında  │
├─────────────────────────────────────────┤
│  📁 Seçili Dosya                        │
│  ✅ program.exe                         │
│  [🔍 EXE Dosyası Seç]                   │
│                                         │
│  [▶️ Çalıştır]                          │
│                                         │
│  📋 Program Çıktısı                     │
│  ┌───────────────────────────────────┐ │
│  │ $ wine program.exe                │ │
│  │ ✅ Program başarıyla çalıştı      │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- PyQt5
- Wine (otomatik kurulur)
- Arch Linux (önerilir)

### Yöntem 1: AppImage (Önerilen)

```bash
# Repoyu klonla
git clone https://github.com/KULLANICI_ADINIZ/ERToS.git
cd ERToS

# AppImage oluştur
chmod +x build-appimage.sh
./build-appimage.sh

# Çalıştır
./ERToS-x86_64.AppImage
```

### Yöntem 2: Hızlı Kurulum

```bash
# Repoyu klonla
git clone https://github.com/RED-FOX-RAB/ERToS.git
cd ERToS

# Kurulum script'ini çalıştır
chmod +x install.sh
./install.sh

# Çalıştır
python3 main.py
```

### Yöntem 3: Manuel Kurulum

```bash
# Bağımlılıkları kur
pip install -r requirements.txt

# Çalıştır
python3 main.py
```

## 📖 Kullanım

### Temel Kullanım

1. **ERToS'u Başlat**
   ```bash
   python3 main.py
   # veya
   ./ERToS-x86_64.AppImage
   ```

2. **İlk Çalıştırma**
   - Wine kurulu değilse otomatik kurulum önerilir
   - "Evet" seçerek Wine'ı otomatik kurun

3. **EXE Dosyası Çalıştırma**
   - "🔍 EXE Dosyası Seç" butonuna tıklayın
   - .exe dosyanızı seçin
   - "▶️ Çalıştır" butonuna tıklayın

### Gelişmiş Özellikler

#### Wine Yapılandırması
```bash
# Ayarlar sekmesinden:
- 🔧 Wine Yapılandırması (winecfg)
- 🎯 Winetricks (ek bileşenler)
- 🔄 Wine'ı Yeniden Kur
```

#### Komut Satırından
```bash
# Direkt wine ile
wine /yol/program.exe

# Wine prefix ile
WINEPREFIX=~/.wine-custom wine program.exe
```

## 🎨 Arayüz Özellikleri

- **Gradient Renkler**: Modern mor-mavi, yeşil, cyan tonları
- **Emoji İkonlar**: Kolay tanımlama için görsel ikonlar
- **Hover Efektleri**: Fare üzerine gelince renk değişimi
- **Terminal Çıktı**: Yeşil yazı, siyah arka plan
- **Responsive Tasarım**: Farklı ekran boyutlarına uyumlu

## 🛠️ Sorun Giderme

### Wine kurulumu başarısız
```bash
sudo pacman -Syu
sudo pacman -S wine winetricks
```

### PyQt5 hatası
```bash
pip install --upgrade PyQt5
```

### AppImage çalışmıyor
```bash
chmod +x ERToS-x86_64.AppImage
# FUSE hatası için:
sudo pacman -S fuse2
```

### .exe dosyası açılmıyor
```bash
# Wine'ı test edin
wine --version

# Wine prefix'i sıfırlayın
rm -rf ~/.wine
```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Commit edin (`git commit -m 'feat: yeni özellik'`)
4. Push edin (`git push origin feature/yeniOzellik`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🌟 Yıldız Verin!

Bu projeyi beğendiyseniz ⭐ vermeyi unutmayın!

## 📞 İletişim

- Issue açarak sorularınızı sorabilirsiniz
- Pull Request göndererek katkıda bulunabilirsiniz

## 🙏 Teşekkürler

- Wine projesi
- PyQt5 ekibi
- Tüm katkıda bulunanlara

---

<div align="center">

**ERToS ile Windows uygulamalarını Linux'ta sorunsuz çalıştırın! 🚀**

Made with ❤️ for Linux users

</div>


