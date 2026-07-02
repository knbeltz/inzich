'''
Pseudocode: 

import openpyxl 
import os 
from date.date import date
from pathlib.path import Path 
from data.models import Company, HistoricalPrice, IncomeStatement, BalanceSheet, CashflowStatement, FinancialRations


def export(
  company: Company,
  historical_prices: List[HistoricalPrice],
  income_statement: IncomeStatement,
  balance_sheet: BalanceSheet,
  cashflow_statement: CashflowStatement,
  financial_ratios: FinancialRatios
  ai_summary: str, 
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
    write_income_statement(income_statement_ws, income_statement)
    write_balance_sheet(balance_sheet_ws, balance_sheet)
    write_cashflow_statement(cashflow_statement_ws, cashflow_statement)
    write_financial_ratios(financial_ratios_ws, financial_ratios)
    write_ai_summary(ai_summary_ws, ai_summary)

    file_path = f"{export_dir}/{ticker.upper()}_{date.today().isoformat()}.xlsx"

    wb.save(file_path)

    os.startfile(file_path) 

    return file_path

def write_income_statement(ws, income_statement):

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

    if not income_statement:
        for row_num, (label, attr_name) in enumerate(metrics, start=2):
            ws.cell(row=row_num, column=1).value = label
        return

    for row_num, (label, attr_name) in enumerate(metrics, start=2):
        ws.cell(row=row_num, column=1).value = label

    for col, statement in enumerate(income_statement, start=2):
        ws.cell(row=1, column=col).value = statement.fiscal_year
        for row_num, (label, attr_name) in enumerate(metrics, start=2):
          value = getattr(statement, attr_name, None)
          ws.cell(row=row_num, column=col).value = value 

    

    
    

'''