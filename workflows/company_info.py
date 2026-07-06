"""End-to-end orchestration for the company report workflow."""

from config.settings import EXPORT_DIR
from ui.prompts import ask_company_name, ask_yes_no, ask_period_type, ask_period_count, quit
from services.company_resolver import resolve_company, CompanyResolverError
from services.yahoo_client import YahooClient
from services.openai_client import get_ai_summary
from data.parsers.company import parse_company
from data.parsers.historical_price import parse_historical_prices
from data.parsers.income_statement import parse_income_statement
from data.parsers.balance_sheet import parse_balance_sheet
from data.parsers.cashflow_statement import parse_cashflow_statement
from data.parsers.financial_ratios import parse_financial_ratios
from exporters.excel_exporter import export
from exporters.ai_summary_exporter import export_ai_summary

def run():
    """Runs the Company Info Workflow"""

    while True:
        error_occurred = False

        # Get a confirmed company
        while True:
            while True:
                user_input = ask_company_name("Enter a company name: ")

                if user_input is None:
                    if quit():
                        return
                    continue

                try:
                    ticker, company_name = resolve_company(user_input)
                    break  # successfully resolved, leave resolver loop

                except CompanyResolverError as e:
                    print(e.message)
                    error_occurred = True
                    break  # leave resolver loop

            if error_occurred:
                break  # leave confirmation loop and go to restart prompt

            confirmed = ask_yes_no(
                f"Do you want to research {company_name} ({ticker})? (Y/N): "
            )

            if confirmed is True:
                break

            elif confirmed is False:
                continue

            elif confirmed is None:
                if quit():
                    return
                continue

        if error_occurred:
            restart = ask_yes_no("Do you want to research another company? (Y/N): ")

            if restart is True:
                continue
            else:
                break

        client = YahooClient(ticker)

        period_type = ask_period_type(
            "What period type would you like to use? (Annual or Quarterly): "
        )

        if period_type is None:
            if quit():
                break
            continue

        period_count = ask_period_count(
            "Enter the number of periods: ",
            period_type,
            4
        )

        if period_count is None:
            if quit():
                break
            continue

        result = client.fetch_all(period_type.lower(), period_count)
        company = parse_company(result.info, ticker)
        historical_prices = parse_historical_prices(result.history, ticker)
        income_statement = parse_income_statement(result.income_stmt, ticker, period_type.lower())
        balance_sheet = parse_balance_sheet(result.balance_sheet, ticker, period_type.lower())
        cashflow_statement = parse_cashflow_statement(result.cash_flow, ticker, period_type.lower())
        financial_ratios = parse_financial_ratios(result.ratios, ticker)

        ai_summary = get_ai_summary(ticker, company_name)

        export(
            company,
            historical_prices,
            income_statement,
            balance_sheet,
            cashflow_statement,
            financial_ratios,
            ticker,
            EXPORT_DIR
        )

        export_ai_summary(ticker, ai_summary, EXPORT_DIR)

        restart = ask_yes_no("Do you want to research another company? (Y/N): ")

        if restart is True:
            continue
        else:
            break