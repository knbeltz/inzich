import pandas as pd
from data.models import CashflowStatement


def parse_cashflow_statement(cash_flow, ticker, period):
    """Builds and returns a list of CashflowStatement objects from the cash_flow DataFrame."""

    cashflow_statements = []

    for index, row in cash_flow.iterrows():
        statement = CashflowStatement(
            ticker=ticker,
            period=period,
            fiscal_year=row["index"].year,
            operating_cash_flow=row.get("Operating Cash Flow"),
            capital_expenditures=row.get("Capital Expenditure"),
            free_cash_flow=row.get("Free Cash Flow"),
            investing_cash_flow=row.get("Investing Cash Flow"),
            financing_cash_flow=row.get("Financing Cash Flow"),
            net_cash_change=row.get("Changes In Cash"),
        )

        cashflow_statements.append(statement)

    return cashflow_statements
