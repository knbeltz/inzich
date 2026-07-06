import os
import platform
import subprocess
from datetime import date 
from pathlib import Path

def export_ai_summary(ticker, ai_summary, export_dir: Path) -> None: 
    
    export_dir.mkdir(parents=True, exist_ok=True)

    file_path = export_dir / f"{ticker}_{date.today().isoformat()}_ai_summary.txt"

    with open(file_path, "w") as f: 
        f.write(ai_summary)

    if platform.system() == "Windows":
        os.startfile(file_path)
    else: 
        subprocess.run(["open", file_path])
        

