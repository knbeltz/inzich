"""Renders the main navigation menu and returns the user's selection."""

from questionary import select

def show_main_menu() -> str:
    options = [
        {"name": "Company Information", "value": "company_info"},
        {"name": "Quit", "value": "quit"},
    ]
    return select("What would you like to do?", choices=options).ask()
