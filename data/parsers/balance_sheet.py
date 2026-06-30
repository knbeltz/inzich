'''
Pseudocode: 

parse_balance_sheet(balance_sheet, ticker, period)

Given a DataFrame, a ticker string, and a period string: 
  Create an empty list to hold results 

  for each row in the dataframe: 
    Build one balance_sheet object using:  
        - ticker and period from the arguments 
        - fiscal_year from row["index"].year 
        - cash from row.get("Cash And Cash Equivalents")
        - inventory from row.get("Inventory")
        - current_assets from row.get("Current Assets")
        - total_assets from row.get("Total Assets")
        - current_liabilities from row.get("Current Liabilities")
        - long_term_debt from row.get("Long Term Debt")
        - total_liabilities from row.get("Total Liabilities Net Minority Interest")
        - shareholders_equity from row.get("Stockholders Equity")
        - any missing column -> None

      Append it to the list 
    
    Return the list

'''

import pandas as pd
from data.models import BalanceSheet

def parse_balance_sheet(balance_sheet, ticker, period): 
    """Build and return a list of BalanceSheet objects from the balance_sheet DataFrame."""
    pass