import pandas as pd
from data.models import HistoricalPrice


def parse_historical_prices(history, ticker):
    """Builds and returns a list of HistoricalPrice objects from the history DataFrame."""

    historical_prices = []

    for date, row in history.iterrows():
        price = HistoricalPrice(
            ticker=ticker,
            date=date.date(),
            open=row.get("Open"),
            high=row.get("High"),
            low=row.get("Low"),
            close=row.get("Close"),
            volume=row.get("Volume"),
            adjusted_close=None,
        )

        historical_prices.append(price)

    return historical_prices
