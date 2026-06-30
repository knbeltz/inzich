'''

Pseudocode: 

parse_financial_ratios(ratios, ticker)

Given a dict of ratios and a ticker string: 
    Build and return one FinancialRatios: 
      - ticker from the argument 
      - pe_ratio from ratios.get("pe_ratio") 
      - forward_pe from ratios.get("forward_pe")
      - roe from ratios.get("roe")
      - roa from ratios.get("roa")
      - debt_equity from ratios.get("debt_equity")
      - current_ratio from ratios.get("current_ratio")
      - quick_ratio from ratios.get("quick_ratio")
      - gross_margin from ratios.get("gross_margin")
      - eps_growth from ratios.get("eps_growth")
      - revenue_growth from ratios.get("revenue_growth")
      - peg_ratio from ratios.get("peg_ratio")
      - operating_margin from ratios.get("operating_margin")
      - profit_margin from ratios.get("profit_margin")
      - any missing column -> None
'''

from data.models import FinancialRatios

def parse_financial_ratios(ratios, ticker):
    """Builds and returns a single FinancialRatios object from the ratios dict."""

    return FinancialRatios(
        ticker=ticker,
        pe_ratio=ratios.get("pe_ratio"),
        forward_pe=ratios.get("forward_pe"),
        roe=ratios.get("roe"),
        roa=ratios.get("roa"),
        debt_equity=ratios.get("debt_equity"),
        current_ratio=ratios.get("current_ratio"),
        quick_ratio=ratios.get("quick_ratio"),
        gross_margin=ratios.get("gross_margin"),
        eps_growth=ratios.get("eps_growth"),
        revenue_growth=ratios.get("revenue_growth"),
        peg_ratio=ratios.get("peg_ratio"),
        operating_margin=ratios.get("operating_margin"),
        profit_margin=ratios.get("profit_margin"),
    )