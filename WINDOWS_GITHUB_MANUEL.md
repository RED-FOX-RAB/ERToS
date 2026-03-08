# Windows'tan GitHub'a Yükleme Rehberi

## Ön Hazırlık

### 1. Git Kurulumu

Git kurulu değilse:
1. https://git-scm.com/download/win adresine git
2. "Download for Windows" tıkla
3. İndir ve kur (varsayılan ayarlarla)

### 2. GitHub Hesabı

GitHub hesabınız yoksa:
1. https://github.com/signup adresine git
2. Hesap oluştur

## Yöntem 1: Otomatik Script (Kolay)

1. `WINDOWS_GITHUB_UPLOAD.bat` dosyasına çift tıkla
2. Kullanıcı adı ve email gir
3. GitHub repository URL'ini gir
4. Şifre/token gir
5. Bitti!

## Yöntem 2: Manuel (PowerShell)

### Adım 1: GitHub'da Repo Oluştur

1. https://github.com/new adresine git
2. Repository name: `ERToS`
3. Description: `Windows .exe dosyalarını Linux'ta çalıştırmak için modern GUI araç`
4. Public seç
5. "Create repository" tıkla

### Adım 2: PowerShell'i Aç

1. ERToS klasörüne sağ tıkla
2. "Open in Terminal" veya "PowerShell'de aç" seç

### Adım 3: Git Komutları

```powershell
# Git yapılandır (ilk kez kullanıyorsanız)
git config --global user.name "KULLANICI_ADINIZ"
git config --global user.email "EMAIL@example.com"

# Repository başlat
git init

# Dosyaları ekle
git add .

# Commit
git commit -m "feat: ERToS v1.0 - Modern GUI ile Windows .exe runner"

# Remote ekle (KULLANICI_ADINIZ'ı değiştir)
git remote add origin https://github.com/KULLANICI_ADINIZ/ERToS.git

# Branch ayarla
git branch -M main

# Push et
git push -u origin main
```

## Yöntem 3: GitHub Desktop (En Kolay)

### Adım 1: GitHub Desktop Kur

1. https://desktop.github.com/ adresine git
2. İndir ve kur
3. GitHub hesabınla giriş yap

### Adım 2: Repo Oluştur

1. File > New Repository
2. Name: `ERToS`
3. Local Path: ERToS klasörünün olduğu yer
4. "Create Repository" tıkla

### Adım 3: Publish

1. "Publish repository" butonuna tıkla
2. Description ekle
3. "Keep this code private" işaretini KALDIR (public olsun)
4. "Publish Repository" tıkla

## Sorun Giderme

### Hata: "Permission denied"

**Çözüm: Personal Access Token kullan**

1. https://github.com/settings/tokens adresine git
2. "Generate new token (classic)" tıkla
3. Note: `ERToS Upload`
4. Expiration: `90 days` veya `No expiration`
5. Scopes: `repo` işaretle
6. "Generate token" tıkla
7. Token'ı KOPYALA (bir daha göremezsiniz!)

Push yaparken:
- Username: GitHub kullanıcı adınız
- Password: Kopyaladığınız TOKEN (şifre değil!)

### Hata: "Repository not found"

Repository URL'ini kontrol edin:
```powershell
git remote -v
```

Düzelt:
```powershell
git remote set-url origin https://github.com/DOGRU_KULLANICI_ADI/ERToS.git
```

### Hata: "Git is not recognized"

Git kurulu değil. Adım 1'e dön.

### Hata: "fatal: not a git repository"

Yanlış klasördesiniz:
```powershell
cd C:\Users\KULLANICI\Desktop\ERToS
```

## Token ile Push (Önerilen)

```powershell
# Token ile push
git push https://TOKEN@github.com/KULLANICI_ADINIZ/ERToS.git main
```

Veya credential helper kullan:
```powershell
git config --global credential.helper wincred
git push
# İlk seferde token gir, sonra hatırlar
```

## Başarılı Yükleme Sonrası

1. https://github.com/KULLANICI_ADINIZ/ERToS adresine git
2. README.md'yi kontrol et
3. Topics ekle:
   - Settings > About > Topics
   - `wine`, `linux`, `pyqt5`, `exe-runner` ekle

4. Social Preview ekle:
   - Settings > Options > Social Preview
   - Görsel yükle (opsiyonel)

## Gelecek Güncellemeler

```powershell
# Değişiklikleri ekle
git add .

# Commit
git commit -m "fix: hata düzeltmesi"

# Push
git push
```

## Yardım

Sorun yaşarsanız:
1. Hata mesajını tam olarak okuyun
2. Google'da aratın: "git [hata mesajı]"
3. GitHub Issue açın

## Başarılar! 🎉

Projeniz GitHub'da olacak:
`https://github.com/KULLANICI_ADINIZ/ERToS`
