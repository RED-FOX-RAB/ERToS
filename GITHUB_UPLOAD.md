# GitHub'a Yükleme Rehberi

## Adım 1: GitHub'da Repo Oluştur

1. https://github.com adresine git
2. Sağ üstteki "+" butonuna tıkla
3. "New repository" seç
4. Repository adı: `ERToS`
5. Açıklama: `Windows .exe dosyalarını Linux'ta çalıştırmak için modern GUI araç`
6. Public seç
7. "Create repository" butonuna tıkla

## Adım 2: Git Kurulumu (Eğer kurulu değilse)

```bash
# Arch Linux
sudo pacman -S git

# Debian/Ubuntu
sudo apt install git
```

## Adım 3: Git Yapılandırması

```bash
# İsim ve email ayarla
git config --global user.name "ADINIZ"
git config --global user.email "EMAIL@example.com"
```

## Adım 4: Projeyi GitHub'a Yükle

```bash
# ERToS klasörüne git
cd ERToS

# Git repository'sini başlat
git init

# Tüm dosyaları ekle
git add .

# İlk commit
git commit -m "feat: ERToS v1.0 - Modern GUI ile Windows .exe runner"

# GitHub repo'nuzu ekleyin (KULLANICI_ADINIZ'ı değiştirin)
git remote add origin https://github.com/KULLANICI_ADINIZ/ERToS.git

# Ana branch'i main olarak ayarla
git branch -M main

# GitHub'a push et
git push -u origin main
```

## Adım 5: GitHub Token ile Yükleme (Önerilir)

Eğer şifre sorunu yaşarsanız:

1. GitHub'da Settings > Developer settings > Personal access tokens
2. "Generate new token (classic)" seç
3. Repo yetkilerini seç
4. Token'ı kopyala
5. Push yaparken şifre yerine token'ı kullan

```bash
# Token ile push
git push https://TOKEN@github.com/KULLANICI_ADINIZ/ERToS.git main
```

## Adım 6: README'yi Güncelle

GitHub'da README.md dosyasını aç ve şu satırları değiştir:

```markdown
# Değiştir:
git clone https://github.com/KULLANICI_ADINIZ/ERToS.git

# Gerçek kullanıcı adınla:
git clone https://github.com/gercekullaniciadi/ERToS.git
```

## Adım 7: Release Oluştur (Opsiyonel)

1. GitHub repo'nuzda "Releases" sekmesine git
2. "Create a new release" tıkla
3. Tag: `v1.0.0`
4. Release title: `ERToS v1.0 - İlk Sürüm`
5. Açıklama ekle
6. "Publish release" tıkla

## Adım 8: Topics Ekle

GitHub repo'nuzda:
1. "About" bölümündeki ⚙️ ikonuna tıkla
2. Topics ekle:
   - `wine`
   - `linux`
   - `exe-runner`
   - `pyqt5`
   - `arch-linux`
   - `gui`
   - `windows-compatibility`

## Gelecek Güncellemeler İçin

```bash
# Değişiklikleri ekle
git add .

# Commit
git commit -m "fix: hata düzeltmesi"

# Push
git push
```

## Sorun Giderme

### "Permission denied" hatası
```bash
# SSH key oluştur
ssh-keygen -t ed25519 -C "email@example.com"

# Public key'i GitHub'a ekle
cat ~/.ssh/id_ed25519.pub
# Çıktıyı GitHub Settings > SSH Keys'e ekle

# SSH ile push
git remote set-url origin git@github.com:KULLANICI_ADINIZ/ERToS.git
git push
```

### "Repository not found" hatası
```bash
# Remote URL'i kontrol et
git remote -v

# Düzelt
git remote set-url origin https://github.com/DOGRU_KULLANICI_ADI/ERToS.git
```

## Başarılı! 🎉

Projeniz artık GitHub'da: `https://github.com/KULLANICI_ADINIZ/ERToS`

Paylaşabilir, yıldız toplayabilir ve katkı alabilirsiniz!
