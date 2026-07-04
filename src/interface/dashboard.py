import subprocess
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_security_scan(file_name):
    path = os.path.join("files_to_scan", file_name)
    # C++ motorunu çağır
    process = subprocess.run(['./scanner', path], capture_output=True, text=True)
    
    if "THREAT_DETECTED" in process.stdout:
        console.print(Panel(f"[bold red]RİSK:[/bold red] {file_name} karantinaya alındı!", title="Zırh Uyarısı"))
    else:
        console.print(Panel(f"[bold green]GÜVENLİ:[/bold green] {file_name} sistem onaylı.", title="Tarama Başarılı"))

console.print("[bold cyan]Armor-Core Güvenlik Sistemi Başlatılıyor...[/bold cyan]")
# Tarama dizinini tara
for f in os.listdir("files_to_scan"):
    if f.endswith(".apk"):
        run_security_scan(f)
