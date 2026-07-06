from datetime import date 
from pathlib import Path

def export_ai_summary(ticker, ai_summary, export_dir: Path) -> None: 
    
    export_dir.mkdir(parents=True, exist_ok=True)

    with open(export_dir / f"{ticker}_{date.today().isoformat()}_ai_summary.txt", "w") as f: 
        f.write(ai_summary)