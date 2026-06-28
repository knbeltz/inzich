"""Renders the splash screen at app startup"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

def show() -> None:
  console = Console()
  
  content = Text(justify="center")
  content.append("INZICH", style="bold #FF9900")
  
  content.append("\n")
  content.append("Built by Kai Beltz", style="#1371FF")
  
  content.append("\n")
  content.append("Powered by OpenAI", style="#FFFFFF")
  
  console.print(Align.center(Panel(content)))