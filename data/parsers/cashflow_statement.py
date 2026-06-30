'''
Pseudocode: 

parse_cashflow_statement(cash_flow, ticker, period)

Given a DataFrame, a ticker string, and a period string: 
  Create an empty list to hold results 

  For each row in the DataFrame: 
    Build one CashflowStatement object using: 
      - ticker and period from the arguments 
      - fiscal_year from row["index"].year 
      - operating_cash_flow from row.get("Operating Cash Flow")
      - capital_expenditures from row.get("Capital Expenditure")
      - free_cash_flow from row.get("Free Cash Flow")
      - investing_cash_flow from row.get("Investing Cash Flow")
      - financing_cash_flow from row.get("Financing Cash Flow")
      - net_cash_change from row.get("Changes In Cash")
      - any missing column -> None
    
    Append it to the list 
  
  Return the list 
'''

import pandas as pd
from data.models import CashflowStatement 

def parse_cashflow_statement(cash_flow, ticker, period): 
    """Builds and returns a list of CashflowStatement objects from the cash_flow DataFrame."""
    pass 