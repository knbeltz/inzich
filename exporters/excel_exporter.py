'''
Pseudocode:

import openpyxl
import os
from datetime import date
from pathlib import Path
from data.models import Company, HistoricalPrice, IncomeStatement, BalanceSheet, CashflowStatement, FinancialRatios


def export(
    company: Company,
    historical_prices: list[HistoricalPrice],
    income_statements: list[IncomeStatement],
    balance_sheets: list[BalanceSheet],
    cash_flows: list[CashflowStatement],
    ratios: FinancialRatios,
    ai_summary: str | None,
    ticker: str,
    export_dir: Path,
) -> Path:

    export_dir.mkdir(parents=True, exist_ok=True)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Company Overview"

    historical_ws = wb.create_sheet("Historical Prices")
    income_statement_ws = wb.create_sheet("Income Statement")
    balance_sheet_ws = wb.create_sheet("Balance Sheet")
    cashflow_statement_ws = wb.create_sheet("Cashflow Statement")
    financial_ratios_ws = wb.create_sheet("Financial Ratios")
    ai_summary_ws = wb.create_sheet("AI Summary")

    write_company_overview(ws, company)
    write_historical_prices(historical_ws, historical_prices)
    write_income_statement(income_statement_ws, income_statements)
    write_balance_sheet(balance_sheet_ws, balance_sheets)
    write_cashflow_statement(cashflow_statement_ws, cash_flows)
    write_financial_ratios(financial_ratios_ws, ratios)
    write_ai_summary(ai_summary_ws, ai_summary)

    file_path = export_dir / f"{ticker.upper()}_{date.today().isoformat()}.xlsx"

    wb.save(file_path)

    os.startfile(file_path)

    return file_path


def write_income_statement(ws, income_statements):

    ws["A1"] = "Metric"

    metrics = [
        ("Revenue", "revenue"),
        ("Gross Profit", "gross_profit"),
        ("Operating Income", "operating_income"),
        ("EBIT", "ebit"),
        ("EBITDA", "ebitda"),
        ("Pretax Income", "pretax_income"),
        ("Net Income", "net_income"),
        ("EPS", "eps"),
    ]

    if not income_statements:
        for row_num, (label, attr_name) in enumerate(metrics, start=2):
            ws.cell(row=row_num, column=1).value = label
        return

    for row_num, (label, attr_name) in enumerate(metrics, start=2):
        ws.cell(row=row_num, column=1).value = label

    for col, statement in enumerate(income_statements, start=2):
        ws.cell(row=1, column=col).value = statement.fiscal_year
        for row_num, (label, attr_name) in enumerate(metrics, start=2):
            value = getattr(statement, attr_name, None)
            ws.cell(row=row_num, column=col).value = value


def write_company_overview(ws, company):
    pass


def write_historical_prices(ws, historical_prices):
    pass


def write_balance_sheet(ws, balance_sheets):
    pass


def write_cashflow_statement(ws, cash_flows):
    pass


def write_financial_ratios(ws, ratios):
    pass


def write_ai_summary(ws, ai_summary):
    pass

'''
