'''
Pseudocode: 

parse_cashflow_statement(cash_flow, ticker, period)

Given a DataFrame, a ticker string, and a period string: 
  Create an empty list to hold results 

  For each row in the DataFrame: 
    Build one CashflowStatement object using: 
      - ticker and period from the arguments 
      - fiscal_year from row["index"].year 
      - operating_cash_flow from row["Operating Cash Flow"]
      - capital_expenditures from row["Capital Expenditures"]
      - free_cash_flow from row["Free Cash Flow"]
      - investing_cash_flow from row["Investing Cash Flow"]
      - financing_cash_flow from row["Financing Cash Flow"]
      - net_cash_change from row["Changes In Cash"]
      - net_cash_chhange from row["Changes In Cash"]
      - any missing column -> None
    
    Append it to the list 
  
  Return it to the list 
'''