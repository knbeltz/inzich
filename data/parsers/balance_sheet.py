'''
Pseudocode: 

parse balance_sheet(balance_sheet, ticker, period)

Given a DataFrame, a ticker string, and a period string: 
  Create an empty list to hold results 

  for each row in the dataframe: 
    Build one balance_sheet object using:  
        - ticker and period from the arguments 
        - fiscal_year from row["index"].year 
        - cash from row["Cash and Cash Equivalents"]
        - inventory from row["Inventory"]
        - current_assets from row["Current Assets"]
        - total_assets from row["Total Assets"]
        - current_liabilities from row["Current Liabilities"]
        - long_term_debt from row["Long Term Debt"]
        - total_liabilities from row["Total Liabilities Net Minority Interest"]
        - shareholders_equity from row["Stockholders Equity"]

'''