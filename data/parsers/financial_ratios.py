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
