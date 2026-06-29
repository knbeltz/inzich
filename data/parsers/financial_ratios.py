'''

Pseudocode: 

parse_finanical_ratios(ratios, ticker)

Given a dict of ratios and a ticker string: 
    Build and return one FinancialRatios: 
      - ticker from the argument
      - all 13 ratio fields directly from the dict using .get() (the keys already match your Pydantic field names - yahoo_client built it that way.) 
'''