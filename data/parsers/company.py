'''
Pseudocode: 

parse_company(info, ticker)

Given a dict of company infor and a ticker string: 
    Build and return one Comapny object using: 
      - ticker from the argument 
      - company_anme from info["longName"]
      - exchange from info["exchange"]
      - all optional fields using info.get() so missing keys return None 
'''