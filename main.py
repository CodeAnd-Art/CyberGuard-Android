import os
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

SCAN_DIR = "./files_to_scan"

def karantinaya_al(file_path):
    """
    Şüpheli dosyayı .virus uzantısıyla yeniden adlandırarak çalışmasını engeller.
    """
    try:
        yeni_ad = file_path + ".virus"
        os.rename(file_path, yeni_ad)
        return True
    except Exception as e:
        logging.error(f"Karantina hatası: {e}")
        return False

def analyze_and_neutralize(file_path, filename):
    """
    Analiz eder ve şüpheliyse anında etkisizleştirir.
    """
    # Basit bir örnek kural: 50KB altı çok şüpheli
    if os.path.getsize(file_path) < 50 * 1024:
        logging.warning(f"!!! TEHLİKE TESPİT EDİLDİ: {filename} !!!")
        if karantinaya_al(file_path):
            logging.info(f"Dosya karantinaya alındı: {filename}.virus")
    else:
        logging.info(f"Dosya temiz: {filename}")

def start_engine():
    if not os.path.exists(SCAN_DIR):
        os.makedirs(SCAN_DIR)
        
    logging.info("--- Güvenlik Zırhı Devrede ---")
    processed_files = set()
    
    while True:
        for file in os.listdir(SCAN_DIR):
            if file.endswith(".apk") and file not in processed_files:
                path = os.path.join(SCAN_DIR, file)
                analyze_and_neutralize(path, file)
                processed_files.add(file)
        time.sleep(3)

if __name__ == "__main__":
    start_engine()
