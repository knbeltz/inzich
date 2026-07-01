"""Reusable input prompt functions for collecting user input across all workflows."""

import questionary 

def ask_company_name(prompt: str) -> str:
    while True:
        result = questionary.text(prompt).ask()
        if result is None:
            return None
        elif not result.strip():
            print("Please enter a valid response.")
        else:
            return result

def ask_yes_no(question: str) -> bool | None: 
    while True: 
        result = questionary.confirm(question).ask()
        if result is None:
            return None
        else: 
            return result
  
def ask_from_list(question: str, options: list) -> str | None: 
    if not options: 
        raise ValueError("No options provided to ask_from_list.")
    while True: 
        result = questionary.select(question, choices=options).ask()
        if result is None:
            return None
        else: 
            return result

def ask_number_of_years(prompt: str) -> int | None: 
    while True:
        result = questionary.text(prompt).ask()
        if result is None:
            return None
        try:
            value = int(result)
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")

'''
Pseudocode: 

def ask_period_type(question) 

    Given a question string: 
        Call ask_from_list with the question and options ["Annual", "Quarterly"]. Return the result (either "Annual", "Quarterly", or None on cancel).

def ask_period_count(question, period_type, max_periods): 

    1. Loop over range(1, max_periods + 1) to build the dict:
   - if period_type == "Annual" and period > 1 → label = f"{period} Years"
   - if period_type == "Annual" and period == 1 → label = f"{period} Year"
   - if period_type == "Quarterly" → label = f"{period}Q"
   - add label → period to the dict

2. Call ask_from_list with the question and the dict keys as options

3. Look up the selected label in the dict, return the int (or None on cancel)

'''
def ask_period_type(question: str) -> str | None:
    """Given a question string, prompts the user to select a period type (Annual or Quarterly). Returns "Annual" or "Quarterly" or None on cancel."""
    return ask_from_list(question, ["Annual", "Quarterly"])

def ask_period_count(question: str, period_type: str, max_periods: int) -> int | None:
    """Given a question string, a period type (Annual or Quarterly), and a maximum number of periods, prompts the user to select a period count. Returns an int or None on cancel."""
    period_dict = {}

    for period in range(1, max_periods +1): 
        if period_type == "Annual" and period > 1:
            label = f"{period} Years"
        elif period_type == "Annual" and period == 1:
            label = f"{period} Year"
        elif period_type == "Quarterly":
            label = f"{period}Q"
        period_dict[label] = period
    
    selected = ask_from_list(question, list(period_dict.keys()))
    
    if selected is None: 
        return None 
    else:
        return period_dict[selected]