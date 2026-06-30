import pandas as pd
from data.models import BalanceSheet


def parse_balance_sheet(balance_sheet, ticker, period):
    """Build and return a list of BalanceSheet objects from the balance_sheet DataFrame."""

    balance_sheets = []

    for index, row in balance_sheet.iterrows():
        statement = BalanceSheet(
            ticker=ticker,
            period=period,
            fiscal_year=row["index"].year,
            cash=row.get("Cash And Cash Equivalents"),
            inventory=row.get("Inventory"),
            current_assets=row.get("Current Assets"),
            total_assets=row.get("Total Assets"),
            current_liabilities=row.get("Current Liabilities"),
            long_term_debt=row.get("Long Term Debt"),
            total_liabilities=row.get("Total Liabilities Net Minority Interest"),
            shareholders_equity=row.get("Stockholders Equity"),
        )

        balance_sheets.append(statement)

    return balance_sheets
