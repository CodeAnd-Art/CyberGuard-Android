#!/bin/bash

# 1. Bildirim
echo "Armor-Core Derleme Süreci Başlatılıyor..."

# 2. C++ Motorlarını birleştir ve derle
# scanner.cpp ve logger.cpp dosyalarını 'scanner' adında tek bir çalıştırılabilir dosyaya dönüştürür
g++ src/engine/scanner.cpp src/engine/logger.cpp -o scanner

# 3. Hata kontrolü
if [ $? -eq 0 ]; then
    echo "C++ Motoru başarıyla derlendi."
else
    echo "HATA: Derleme başarısız oldu. Lütfen kodları kontrol et."
    exit 1
fi

# 4. Python bağımlılıklarını kur
pip install -r requirements.txt

# 5. Başarı mesajı
echo "------------------------------------------------"
echo "Armor-Core Sistemi Hazır!"
echo "Başlatmak için şu komutu yaz: python3 src/interface/dashboard.py"
echo "------------------------------------------------"

