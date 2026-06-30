'''
Pseudocode: 

parse_company(info, ticker)

Given a dict of company info and a ticker string: 
    Build and return one Company object using: 
      - ticker from the argument 
      - company_name from info.get("longName")
      - exchange from info.get("exchange")
      - sector from info.get("sector")
      - industry from info.get("industry")
      - country from info.get("country")
      - employees from info.get("fullTimeEmployees")
      - market_cap from info.get("marketCap")
      - enterprise_value from info.get("enterpriseValue")
      - current_price from info.get("currentPrice")
      - currency from info.get("currency")
      - shares_outstanding from info.get("sharesOutstanding")
      - beta from info.get("beta")
      - dividend_yield from info.get("dividendYield")
      - week_52_high from info.get("fiftyTwoWeekHigh")
      - week_52_low from info.get("fiftyTwoWeekLow")
      - any missing column -> None

        Append it to the list 

    Return the list 

'''

from data.models import Company 

def parse_company(info, ticker):
    """Builds and returns a single Company object from the info dict."""
    pass