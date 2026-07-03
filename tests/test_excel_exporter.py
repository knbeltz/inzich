"""Manual smoke test for the Excel exporter — run directly to verify the workbook opens."""

from pathlib import Path
from data.models import (
    Company, HistoricalPrice, IncomeStatement, BalanceSheet,
    CashflowStatement, FinancialRatios,
)
from exporters.excel_exporter import export
from datetime import date

company = Company(
    ticker="AAPL",
    company_name="Apple Inc.",
    exchange="NASDAQ",
    sector="Technology",
    industry="Consumer Electronics",
    country="United States",
    employees=161000,
    market_cap=2_800_000_000_000.0,
    enterprise_value=2_750_000_000_000.0,
    current_price=185.50,
    currency="USD",
    shares_outstanding=15_550_000_000.0,
    beta=1.24,
    dividend_yield=0.005,
    week_52_high=199.62,
    week_52_low=124.17,
)

historical_prices = [
    HistoricalPrice(ticker="AAPL", date=date(2024, 1, 1), open=185.0, high=187.0, low=184.0, close=186.0, adjusted_close=186.0, volume=52_000_000.0),
    HistoricalPrice(ticker="AAPL", date=date(2024, 1, 2), open=186.0, high=188.0, low=185.0, close=187.0, adjusted_close=187.0, volume=48_000_000.0),
]

income_statements = [
    IncomeStatement(ticker="AAPL", period="annual", fiscal_year=2024, revenue=391_035_000_000.0, gross_profit=180_683_000_000.0, operating_income=123_216_000_000.0, ebit=123_216_000_000.0, ebitda=137_352_000_000.0, pretax_income=125_820_000_000.0, net_income=93_736_000_000.0, eps=6.11),
    IncomeStatement(ticker="AAPL", period="annual", fiscal_year=2023, revenue=383_285_000_000.0, gross_profit=169_148_000_000.0, operating_income=114_301_000_000.0, ebit=114_301_000_000.0, ebitda=128_263_000_000.0, pretax_income=113_736_000_000.0, net_income=96_995_000_000.0, eps=6.16),
]

balance_sheets = [
    BalanceSheet(ticker="AAPL", period="annual", fiscal_year=2024, cash=29_965_000_000.0, inventory=7_286_000_000.0, current_assets=152_987_000_000.0, total_assets=364_980_000_000.0, current_liabilities=176_392_000_000.0, long_term_debt=85_750_000_000.0, total_liabilities=308_030_000_000.0, shareholders_equity=56_950_000_000.0),
    BalanceSheet(ticker="AAPL", period="annual", fiscal_year=2023, cash=29_965_000_000.0, inventory=6_331_000_000.0, current_assets=143_566_000_000.0, total_assets=352_583_000_000.0, current_liabilities=145_308_000_000.0, long_term_debt=95_281_000_000.0, total_liabilities=290_437_000_000.0, shareholders_equity=62_146_000_000.0),
]

cash_flows = [
    CashflowStatement(ticker="AAPL", period="annual", fiscal_year=2024, operating_cash_flow=118_254_000_000.0, capital_expenditures=-9_447_000_000.0, free_cash_flow=108_807_000_000.0, investing_cash_flow=-53_950_000_000.0, financing_cash_flow=-69_895_000_000.0, net_cash_change=-5_591_000_000.0),
    CashflowStatement(ticker="AAPL", period="annual", fiscal_year=2023, operating_cash_flow=113_260_000_000.0, capital_expenditures=-10_959_000_000.0, free_cash_flow=102_301_000_000.0, investing_cash_flow=-34_037_000_000.0, financing_cash_flow=-108_488_000_000.0, net_cash_change=-29_265_000_000.0),
]

ratios = FinancialRatios(
    ticker="AAPL",
    pe_ratio=28.5,
    forward_pe=25.1,
    peg_ratio=2.8,
    roe=1.47,
    roa=0.28,
    debt_equity=1.87,
    current_ratio=0.99,
    quick_ratio=0.97,
    gross_margin=0.46,
    operating_margin=0.31,
    profit_margin=0.24,
    revenue_growth=0.02,
    eps_growth=0.08,
)

export(
    company=company,
    historical_prices=historical_prices,
    income_statements=income_statements,
    balance_sheets=balance_sheets,
    cash_flows=cash_flows,
    ratios=ratios,
    ai_summary="Apple Inc. continues to lead the consumer electronics market with strong services revenue growth.\n\nSources:\n1. Bloomberg, 'Apple Q4 2024 Results', 2024\n2. Reuters, 'iPhone 16 demand outlook', 2024",
    ticker="AAPL",
    export_dir=Path("exports"),
)
