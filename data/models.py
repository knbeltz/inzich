"""Pydantic data models — shared contract between parsers and exporters."""

from datetime import date
from typing import Literal 
from pydantic import BaseModel 

class CompanyBase(BaseModel): 
    ticker: str 


class FinancialStatementBase(CompanyBase): 
    period: Literal["annual", "quarterly"]
    fiscal_year: int

class Company(CompanyBase): 
    company_name: str 
    exchange: str 
    sector: str | None = None
    industry: str | None = None 
    country: str | None = None
    employees: int | None = None
    market_cap: float | None = None 
    enterprise_value: float | None = None
    current_price: float | None = None
    currency: str | None = None
    shares_outstanding: float | None = None
    beta: float | None = None
    dividend_yield: float | None = None
    week_52_high: float | None = None
    week_52_low: float | None = None

class HistoricalPrice(CompanyBase): 
    date: date
    open: float | None = None
    high: float | None = None
    low: float | None = None 
    close: float | None = None
    adjusted_close: float | None = None
    volume: float | None = None

class IncomeStatement(FinancialStatementBase):
    revenue: float | None = None
    gross_profit: float | None = None
    operating_income: float | None = None
    ebit: float | None = None
    ebitda: float | None = None
    pretax_income: float | None = None
    net_income: float | None = None
    eps: float | None = None

class BalanceSheet(FinancialStatementBase):
    cash: float | None = None
    inventory: float | None = None
    current_assets: float | None = None
    total_assets: float | None = None
    current_liabilities: float | None = None
    long_term_debt: float | None = None
    total_liabilities: float | None = None
    shareholders_equity: float | None = None

class CashflowStatement(FinancialStatementBase):
    operating_cash_flow: float | None = None
    capital_expenditures: float | None = None
    free_cash_flow: float | None = None
    investing_cash_flow: float | None = None
    financing_cash_flow: float | None = None
    net_cash_change: float | None = None

class FinancialRatios(CompanyBase):
    pe_ratio: float | None = None
    forward_pe: float | None = None
    peg_ratio: float | None = None
    roe: float | None = None
    roa: float | None = None
    debt_equity: float | None = None
    current_ratio: float | None = None
    quick_ratio: float | None = None
    gross_margin: float | None = None
    operating_margin: float | None = None
    profit_margin: float | None = None
    revenue_growth: float | None = None
    eps_growth: float | None = None
