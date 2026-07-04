import os
import time
import logging

# Logları hem terminale hem de bir dosyaya yazdırır
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[logging.FileHandler("scanner_log.log"), logging.StreamHandler()]
)

# Codespaces veya yerel dizin için esnek yol
SCAN_DIR = os.getenv("SCAN_DIR", "./files_to_scan")

def perform_scan(file_path):
    """Burada dosya analizi mantığını (signature, heuristic) geliştirebilirsin."""
    try:
        file_size = os.path.getsize(file_path)
        # Basit bir kontrol: 50KB altı dosyalar genellikle boş veya zararlı olabilir
        if file_size < 50 * 1024:
            return "ŞÜPHELİ (Düşük Boyut)"
        return "TEMİZ"
    except Exception as e:
        return f"HATA: {e}"

def start_engine():
    logging.info("--- Antivirüs Zırhı Aktif ---")
    if not os.path.exists(SCAN_DIR):
        os.makedirs(SCAN_DIR)
        logging.info(f"Tarama dizini oluşturuldu: {SCAN_DIR}")

    processed_files = set()
    
    while True:
        try:
            for file in os.listdir(SCAN_DIR):
                if file.endswith(".apk") and file not in processed_files:
                    path = os.path.join(SCAN_DIR, file)
                    status = perform_scan(path)
                    logging.info(f"Dosya: {file} | Sonuç: {status}")
                    processed_files.add(file)
        except Exception as e:
            logging.error(f"Sistem hatası: {e}")
        time.sleep(5)

if __name__ == "__main__":
    start_engine()
