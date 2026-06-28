
import yfinance as yf 
import pandas as pd 
from dataclasses import dataclass
from typing import Any

class YahooClientError(Exception): 
    def __init__(self, ticker, message): 
        """Raised when yfinance returns empty data for a confirmed ticker."""
        self.ticker = ticker 
        self.message = message
        super().__init__(message)

@dataclass 
class FetchResult: 
    info: dict[str, Any]
    history: pd.DataFrame
    income_stmt: pd.DataFrame
    balance_sheet: pd.DataFrame
    cash_flow: pd.DataFrame
    ratios: dict[str, Any]

class YahooClient:
    def __init__(self, ticker):
        """Initializes the client with a ticker symbol and creates the yfinance Ticker object."""
        self.ticker = ticker.upper().strip()
        self._yf_ticker = yf.Ticker(self.ticker)

    def fetch_all(self, period: str, num_periods: int) -> FetchResult:
        """Fetches all 6 data types from Yahoo Finance and returns a cleaned FetchResult."""
        info = self._yf_ticker.info

        if not info:
            raise YahooClientError(self.ticker, "No info found for ticker")

        history = self._yf_ticker.history(period="max")

        if period == "annual":
            income_stmt = self._yf_ticker.financials
            balance_sheet = self._yf_ticker.balance_sheet
            cash_flow = self._yf_ticker.cashflow
            rows = num_periods * 252
            history = history.tail(rows)
        else:
            income_stmt = self._yf_ticker.quarterly_financials
            balance_sheet = self._yf_ticker.quarterly_balance_sheet
            cash_flow = self._yf_ticker.quarterly_cashflow
            rows = num_periods * 63
            history = history.tail(rows)

        ratios = {
            "pe_ratio": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "peg_ratio": info.get("pegRatio"),
            "roe": info.get("returnOnEquity"),
            "roa": info.get("returnOnAssets"),
            "debt_equity": info.get("debtToEquity"),
            "current_ratio": info.get("currentRatio"),
            "quick_ratio": info.get("quickRatio"),
            "gross_margin": info.get("grossMargins"),
            "operating_margin": info.get("operatingMargins"),
            "profit_margin": info.get("profitMargins"),
            "eps_growth": info.get("earningsGrowth"),
            "revenue_growth": info.get("revenueGrowth"),      
        }

        income_stmt = income_stmt.T.reset_index()
        balance_sheet = balance_sheet.T.reset_index()
        cash_flow = cash_flow.T.reset_index()

        return FetchResult(
            info=info, 
            history=history, 
            income_stmt=income_stmt, 
            balance_sheet=balance_sheet, 
            cash_flow=cash_flow, 
            ratios=ratios
            )

     

    

