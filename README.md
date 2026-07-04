# Antivirus Armor
Otomatik APK tarama, analiz ve karantina sistemi.

## Kurulum ve Çalıştırma
1. Tarama dizinini oluşturun: `mkdir files_to_scan`
2. Sistemi başlatın: `python main.py`

## Çalışma Prensibi
Sistem, `files_to_scan` klasörünü sürekli izler. Şüpheli gördüğü APK dosyalarını `.virus` uzantısına çevirerek etkisiz kılar.
