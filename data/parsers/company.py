'''
Pseudocode: 

parse_company(info, ticker)

Given a dict of company info and a ticker string: 
    Build and return one Company object using: 
      - ticker from the argument 
      - company_name from info["longName"]
      - exchange from info["exchange"]
      - all optional fields using info.get() so missing keys return None 
'''