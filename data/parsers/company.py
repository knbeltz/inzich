from data.models import Company


def parse_company(info, ticker):
    """Builds and returns a single Company object from the info dict."""

    return Company(
        ticker=ticker,
        company_name=info["longName"],
        exchange=info["exchange"],
        sector=info.get("sector"),
        industry=info.get("industry"),
        country=info.get("country"),
        employees=info.get("fullTimeEmployees"),
        market_cap=info.get("marketCap"),
        enterprise_value=info.get("enterpriseValue"),
        current_price=info.get("currentPrice"),
        currency=info.get("currency"),
        shares_outstanding=info.get("sharesOutstanding"),
        beta=info.get("beta"),
        dividend_yield=info.get("dividendYield"),
        week_52_high=info.get("fiftyTwoWeekHigh"),
        week_52_low=info.get("fiftyTwoWeekLow"),
    )
