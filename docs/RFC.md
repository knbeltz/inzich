# Inzich V1 — RFC (Architecture & Decisions)

> Updated after every approved phase sign-off.

---

## What Inzich Is

A Python terminal app that fetches financial data for any public company from Yahoo Finance and exports it as a professional multi-sheet Excel workbook. V1 is a single workflow: one company in, one `.xlsx` out.

---

## Technology Stack

| Package | Version | Role |
|---|---|---|
| Python | 3.11.3 | Runtime |
| rich | >=13.0.0 | Terminal UI: colors, panels, spinners |
| questionary | >=2.0.0 | Interactive prompts: select, confirm, text, checkbox |
| python-dotenv | >=1.0.0 | Load `.env` into `os.environ` |
| yfinance | >=0.2.0 | PRIMARY data source — all financial statements |
| pandas | >=2.0.0 | DataFrames; yfinance returns DataFrames |
| numpy | >=1.24.0 | Numerical operations on financial arrays |
| pydantic | >=2.0.0 | Data models with built-in validation |
| openpyxl | >=3.1.0 | Excel workbook generation |
| openai | >=1.0.0 | Optional Sheet 7 AI research summary |
| requests | >=2.31.0 | HTTP — yfinance internals dependency |
| sqlite3 | stdlib | Caching layer (no extra install needed) |
| pytest | >=7.4.0 | Test framework |
| pytest-mock | >=3.11.0 | Mock yfinance in unit tests |

---

## Folder Architecture

```
inzich/
├── config/settings.py        One place for all env vars. Nothing else reads .env directly.
├── ui/                        All terminal rendering. Workflows call UI — never the reverse.
│   ├── splash.py
│   ├── menus.py
│   └── prompts.py
├── services/                  One client per external system. Swappable, mockable.
│   ├── yahoo_client.py        PRIMARY: all financial data
│   ├── company_resolver.py    Search + ticker confirmation
│   └── openai_client.py       Optional Sheet 7 AI summary
├── workflows/
│   └── company_info.py        Orchestration only — calls services + UI, no business logic
├── data/
│   ├── models.py              Pydantic models: shared contract between parsers and exporters
│   ├── cache.py               SQLite, 24hr TTL per ticker
│   └── parsers/               yfinance dicts → clean Pydantic models, one file per statement
├── exporters/
│   └── excel_exporter.py      Knows only Pydantic models → openpyxl. No API knowledge.
└── utils/
    ├── logger.py
    └── validators.py
```

---

## Key Architectural Decisions

### 1. Yahoo Finance as primary data source (not SEC EDGAR)
yfinance provides all data needed for V1 without an API key. EDGAR integration adds significant complexity (CIK lookup, XBRL parsing) with no V1 benefit. Deferred to V2.

### 2. No FRED API in V1
FRED is only needed for WACC (risk-free rate, market return premium). DCF and WACC are V2 features. `fredapi` removed from requirements entirely.

### 3. No vector database
EDGAR data is structured XBRL with known field names — semantic search is not needed. SQLite is sufficient for caching purposes.

### 4. SQLite for caching only
Cache stores raw yfinance responses keyed by ticker with a 24-hour TTL. Not used for application state.

### 5. Pydantic models as the shared contract
Parsers produce Pydantic models. The exporter consumes Pydantic models. This means parsers and the exporter never need to know about each other and can be tested independently.

### 6. questionary returns None on Ctrl+C
questionary catches `KeyboardInterrupt` internally and returns `None` instead of propagating. All prompt functions in `ui/prompts.py` return `None` on cancel — they do not call `sys.exit()`. The main loop handles `None` returns with a quit confirmation.

### 7. Fail-fast config
`config/settings.py` raises `ValueError` immediately on startup if any required env var is missing. The app never starts in a half-configured state.

### 8. Named logger (`"inzich"`)
One logger named `"inzich"` used across all modules via `from utils.logger import logger`. Named loggers let all modules share the same handlers without re-configuring.

### 9. OpenAI API key is optional
`OPENAI_API_KEY` is required only for Sheet 7. If the key is missing at startup, the app warns the user and continues — it does not crash. Sheet 7 is silently excluded from the sheet selection menu when the key is absent. The fail-fast rule in `config/settings.py` applies only to truly required vars (`DB_PATH`, `EXPORT_DIR`).

### 10. Company name validation via OpenAI
yfinance has no search API — you must already know the exact ticker. OpenAI handles fuzzy resolution: it takes the user's free-text input (which may be misspelled, gibberish, or multiple companies) and returns either a confirmed ticker + canonical name or a structured error. This means the user never needs to know a ticker symbol. Error cases handled: unrecognized company, not publicly traded, multiple companies entered at once, gibberish.

### 11. Annual vs quarterly data period — no sheet selection
After company confirmation, the user selects annual or quarterly, then the number of periods. Annual is capped at 4 years; quarterly at 16 quarters. Availability is checked first and the cap is lowered if fewer periods exist. All 7 sheets are always exported — the user makes no sheet selection. Sheet 7 is included automatically if `OPENAI_API_KEY` is present, skipped silently if not. The Yahoo Finance client always fetches all 6 data types via a single `fetch_all()` call.

### 12. Sheet 7 uses OpenAI with web search and citations
The AI summary (Sheet 7) is generated via an OpenAI call that uses the `web_search_preview` tool so it can pull current information beyond the training cutoff. The response must include cited sources, which are parsed and written into the sheet as a numbered reference list.

---

## Development Workflow (9 Steps per Phase)

Each phase follows this sequence:

1. **Requirements** — What does this module need to do? Edge cases?
2. **Architecture** — Where does it live? What does it call/return?
3. **Pseudocode** — Write logic in plain English before touching code
4. **Scaffold** — Create file with docstring + `pass`-body stubs
5. **Draft** — Implement the code
6. **Review** — Mentor reviews for correctness, edge cases, style
7. **Fix** — Engineer corrects all flagged issues
8. **Verify** — Run the code / tests; confirm it works
9. **Sign-off** — Mentor approves; RFC updated; move to next phase

---

## Phase Status

| Phase | Status | Name |
|---|---|---|
| 1 | ✅ Complete | Project Setup |
| 2 | ✅ Complete | Configuration (`config/settings.py`) |
| 3 | ✅ Complete | Logging (`utils/logger.py`) |
| 4 | ✅ Complete | UI Foundation (`splash.py`, `menus.py`, `main.py`) |
| 5 | ✅ Complete | Input Handling (`ui/prompts.py`) |
| 6 | ✅ Complete | Main App Loop Update |
| 7 | ✅ Complete | Yahoo Finance Client |
| 8 | ✅ Complete | Company Search + Validation |
| 9 | ✅ Complete | Data Models |
| 10 | ⬜ | Data Parsers |
| 11 | ⬜ | Period Selection UI |
| 12 | ⬜ | Excel Exporter |
| 13 | ⬜ | Optional AI Summary |
| 14 | ⬜ | Company Report Workflow |
| 15 | ⬜ | Caching Layer |
| 16 | ⬜ | Error Handling + Polish |
| 17 | ⬜ | Unit Tests |
| 18 | ⬜ | Integration Tests |
| 19 | ⬜ | Documentation |

---

## Data Schema

### Company
```python
ticker, company_name, exchange, sector, industry, country, employees,
market_cap, enterprise_value, current_price, currency, shares_outstanding,
beta, dividend_yield, week_52_high, week_52_low
```

### HistoricalPrice
```python
ticker, date, open, high, low, close, adjusted_close, volume
```

### IncomeStatement
```python
ticker, period, fiscal_year, revenue, gross_profit, operating_income, ebit,
ebitda, pretax_income, net_income, eps
# period: "annual" | "quarterly"
```

### BalanceSheet
```python
ticker, period, fiscal_year, cash, inventory, current_assets, total_assets,
current_liabilities, long_term_debt, total_liabilities, shareholders_equity
# period: "annual" | "quarterly"
```

### CashFlowStatement
```python
ticker, period, fiscal_year, operating_cash_flow, capital_expenditures,
free_cash_flow, investing_cash_flow, financing_cash_flow, net_cash_change
# period: "annual" | "quarterly"
```

### FinancialRatios
```python
ticker, pe_ratio, forward_pe, peg_ratio, roe, roa, debt_equity,
current_ratio, quick_ratio, gross_margin, operating_margin,
profit_margin, revenue_growth, eps_growth
```
