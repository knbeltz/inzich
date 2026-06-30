import pandas as pd
from data.models import IncomeStatement


def parse_income_statement(income_stmt, ticker, period):
    """Builds and returns a list of IncomeStatement objects from the income_stmt DataFrame."""

    statements = []

    for index, row in income_stmt.iterrows():
        statement = IncomeStatement(
            ticker=ticker,
            period=period,
            fiscal_year=row["index"].year,
            revenue=row.get("Total Revenue"),
            gross_profit=row.get("Gross Profit"),
            operating_income=row.get("Operating Income"),
            ebit=row.get("EBIT"),
            ebitda=row.get("EBITDA"),
            pretax_income=row.get("Pretax Income"),
            net_income=row.get("Net Income"),
            eps=row.get("Diluted EPS"),
        )

        statements.append(statement)

    return statements
