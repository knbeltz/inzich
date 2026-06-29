'''
Pseudocode: 

parse_income_statement(income_stmt, ticker, period)

Given a DataFrame, a ticker string, and a period string: 
  Create an empty list to hold results  

  For each row in the DataFrame: 
    Build one IncomeStatement object using: 
      - ticker and period from the arguments 
      - fiscal_year from row["index"].year
      - revenue from row["Total Revenue"]
      - gross_profit from row["Gross Profit"]
      - operating_income from row["Operating Income"]
      - ebit from row["EBIT"]
      - ebitda from row["EBITDA"]
      - pretax_income from row["Pretax Income"]
      - net_income from row["Net Income"]
      - eps from row["Diluted EPS"]
      - any missing column -> None

    Append it to the list 
  
  Return the list 

'''