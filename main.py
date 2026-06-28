"""Entry point for the Inzich application."""

import config.settings
import questionary
from utils.logger import logger
from ui.splash import show
from ui.menus import show_main_menu

show()

while True:
    try:
        selection = show_main_menu()

        if selection is None:
            confirmed = questionary.confirm("Are you sure you want to quit?").ask()
            if confirmed:
                break

        elif selection == "company_info":
            logger.info("User selected Company Info")
            print("Company Info workflow coming soon...")

        elif selection == "quit":
            break

    except KeyboardInterrupt:
        answer = questionary.confirm("Are you sure you want to quit?").ask()
        if answer:
            break
