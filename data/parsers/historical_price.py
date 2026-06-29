'''
Psuedocode:

parse_historical_prices(history, ticker)

Given a DataFrame of price history and a ticker string: 
    Create an empty list to hold results. 

    For each row in the DataFrame: 
        Build one Historical Price object using: 
            - ticker from the argument 
            - date from the row's index (the DataFrame index is the date here.)
            - open, high, low, close, volume from the row's columns 
            - adjusted_close = None (yfinance doesn't return it seperately) 

        Append it to the list.
    Return the list. 
'''