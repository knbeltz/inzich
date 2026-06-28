'''
Initital Questions: 

1. With pydantic field: float | None

2. Literal["annual", "quarterly"]

3. datetime.date

4. Configure it with an or statement where it can be a float or a None value with Pydantic. 

5. Int 
. 
'''

''' 
Pesudocode 

CompanyBase inherets from Pydantic BaseModel 
    -ticker: str 

FinancialStatementBase inhereits from CompanyBase: 
    - period: Literal["annual", "quarterly"]
    - fiscal_year: int

Company inherits from CompanyBase: 
    - company_name: str 
    - exchange: str 
    - sector: str | None
    - industry: str | None
    - country: str | None
    - employees: int | None
    - market_cap: float | None
    - enterprise_value: float | None
    - current_price: float | None
    - currency: str | None
    - shares_outstanding: float | None
    - beta: float | None
    - dividend_yield: float | None
    - week_52_high: float | None
    - week_52_low: float | None
  
HistoricalPrice inherits from CompanyBase: 
    - date: datetime.date
    - open: float | None
    - high: float | None
    - low: float | None
    - close: float | None
    - adjusted_close: float | None
    - volume: float | None

IncomeStatment inherits from FinancialStatementBase: 
    - revenue: float | None
    - gross_profit: float | None
    - operating_income: float | None
    - ebit: float | None
    - ebitda: float | None
    - pretax_income: float | None
    - net_income: float | None
    - eps: float | None 

BalanceSheet inherits from FinancialStatementBase: 
    - cash: float | None
    - inventory: float | None
    - current_assets: float | None
    - total_assets: float | None
    - current_liabilities: float | None
    - long_term_debt: float | None
    - total_liabilities: float | None
    - shareholders_equity: float | None  

CashflowStatement inherits from FinancialStatementBase: 
    - operating_cash_flow: float | None
    - capital_expenditures: float | None
    - free_cash_flow: float | None
    - investing_cash_flow: float | None
    - financing_cash_flow: float | None
    - net_cash_change: float | None

FinancialRatios inherits from CompanyBase: 
    - pe_ratio: float | None
    - forward_pe: float | None
    - peg_ratio: float | None
    - roe: float | None
    - roa: float | None
    - debt_equity: float | None
    - current_ratio: float | None
    - quick_ratio: float | None
    - gross_margin: float | None
    - operating_margin: float | None
    - profit_margin: float | None
    - revenue_growth: float | None
    - eps_growth: float | None
'''

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
