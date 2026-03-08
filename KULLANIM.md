# ERToS Kullanım Kılavuzu

## Hızlı Başlangıç

### Linux'ta (Arch)

1. **Hızlı Kurulum:**
```bash
cd ERToS
chmod +x install.sh
./install.sh
```

2. **Çalıştırma:**
```bash
python3 main.py
```

3. **AppImage Oluşturma:**
```bash
chmod +x build-appimage.sh
./build-appimage.sh
# Oluşan ERToS-x86_64.AppImage dosyasını çalıştırın
./ERToS-x86_64.AppImage
```

### Windows'ta Test (Geliştirme)

```cmd
run.bat
```

## Detaylı Kullanım

### İlk Çalıştırma

1. ERToS'u başlattığınızda Wine kontrolü yapılır
2. Wine kurulu değilse otomatik kurulum önerilir
3. "Evet" diyerek Wine'ı otomatik kurabilirsiniz

### EXE Dosyası Çalıştırma

1. "EXE Dosyası Seç" butonuna tıklayın
2. Çalıştırmak istediğiniz .exe dosyasını seçin
3. "Çalıştır" butonuna tıklayın
4. Program çıktısı alt panelde görünecektir

### Wine Ayarları

**Ayarlar** sekmesinden:

- **Wine Yapılandırması**: Wine ayarlarını düzenleyin (winecfg)
- **Winetricks**: Ek Windows bileşenleri kurun
- **Wine'ı Yeniden Kur**: Sorun yaşarsanız Wine'ı yeniden kurun

### Desteklenen Dosya Türleri

- .exe (Windows çalıştırılabilir)
- .msi (Windows yükleyici - Wine ile)
- .bat (Batch dosyaları)

## İpuçları

### Wine Prefix Yönetimi

Her uygulama için ayrı Wine prefix kullanmak istiyorsanız:

```bash
WINEPREFIX=~/.wine-uygulamam wine program.exe
```

### DirectX Gerektiren Oyunlar

```bash
winetricks d3dx9 dxvk
```

### .NET Framework Gerektiren Uygulamalar

```bash
winetricks dotnet48
```

### Ses Sorunları

```bash
winetricks sound=alsa
# veya
winetricks sound=pulse
```

## Sık Karşılaşılan Sorunlar

### "Wine bulunamadı" hatası

```bash
sudo pacman -S wine
```

### PyQt5 hatası

```bash
pip install --user PyQt5
```

### Uygulama açılmıyor

1. Terminal'den çalıştırıp hata mesajlarını kontrol edin:
```bash
python3 main.py
```

2. Wine'ı test edin:
```bash
wine --version
```

### AppImage çalışmıyor

```bash
chmod +x ERToS-x86_64.AppImage
./ERToS-x86_64.AppImage
```

FUSE hatası alırsanız:
```bash
sudo pacman -S fuse2
```

## Gelişmiş Kullanım

### Komut Satırından EXE Çalıştırma

```bash
wine /yol/program.exe
```

### Wine Sürümünü Değiştirme

```bash
# Wine Staging (daha yeni özellikler)
sudo pacman -S wine-staging

# Wine GE (oyunlar için optimize)
# AUR'dan kurulabilir
```

### Performans İyileştirme

```bash
# DXVK (DirectX to Vulkan)
winetricks dxvk

# Esync etkinleştir
echo "WINEESYNC=1" >> ~/.bashrc
```

## Dosya İlişkilendirme

.exe dosyalarını ERToS ile otomatik açmak için:

```bash
xdg-mime default ertos.desktop application/x-ms-dos-executable
```

## Kaldırma

```bash
# Manuel kurulum
rm -rf ~/.local/share/applications/ertos.desktop
rm -rf ~/ERToS

# Wine'ı da kaldırmak isterseniz
sudo pacman -R wine
```

## Destek

Sorun yaşarsanız:
1. README.md dosyasını okuyun
2. Wine loglarını kontrol edin: `~/.wine/`
3. Terminal çıktısını inceleyin

## Güncellemeler

Yeni sürüm kontrolü:
```bash
cd ERToS
git pull  # Eğer git repo'sundan kurduysanız
```
