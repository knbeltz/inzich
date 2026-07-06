# Inzich — Project Context

Technical reference for contributors. Covers architecture decisions, development workflow, and current project state.

---

## What Inzich Is

A Python terminal app that fetches financial data for any publicly traded company from Yahoo Finance and exports a professional 6-sheet Excel workbook plus an AI-generated research summary. V1 is a single workflow: user enters a company name → app fetches data → exports `.xlsx` and `.txt`.

---

## Technology Stack

| Package | Version | Role |
|---|---|---|
| Python | 3.11.3 | Runtime |
| rich | >=13.0.0 | Terminal UI: colors, panels, spinners |
| questionary | >=2.0.0 | Interactive prompts: select, confirm, text |
| python-dotenv | >=1.0.0 | Load `.env` into `os.environ` |
| yfinance | >=0.2.0 | PRIMARY data source — all financial statements |
| pandas | >=2.0.0 | DataFrames; yfinance returns DataFrames |
| numpy | >=1.24.0 | Numerical operations on financial arrays |
| pydantic | >=2.0.0 | Data models with built-in validation |
| openpyxl | >=3.1.0 | Excel workbook generation |
| openai | >=1.0.0 | Company resolution + AI summary |
| sqlite3 | stdlib | Caching layer (no extra install needed) |
| pytest | >=7.4.0 | Test framework |
| pytest-mock | >=3.11.0 | Mock yfinance in unit tests |

---

## Key Architectural Decisions

### 1. Yahoo Finance as primary data source
yfinance provides all data needed for V1 without an API key. SEC EDGAR integration is deferred to V2.

### 2. Pydantic models as the shared contract
Parsers produce Pydantic models. The exporter consumes Pydantic models. Parsers and exporters never need to know about each other and can be tested independently.

### 3. questionary returns None on Ctrl+C
questionary catches `KeyboardInterrupt` internally and returns `None`. All prompt functions in `ui/prompts.py` return `None` on cancel — they never call `sys.exit()`. The main loop handles `None` with a quit confirmation.

### 4. Fail-fast config
`config/settings.py` raises `ValueError` immediately on startup if any required env var is missing. `OPENAI_API_KEY` is required — used for both company resolution and AI summary.

### 5. Company name validation via OpenAI
yfinance has no search API. OpenAI resolves free-text input to a confirmed ticker. Handles misspellings, gibberish, multiple companies entered at once, and companies that are not publicly traded.

### 6. Period capped at 4 years / 4 quarters
Yahoo Finance reliably returns up to 4 annual or 4 quarterly periods. Options are hardcoded to this cap rather than dynamically fetching available periods.

### 7. AI summary exported as .txt
The AI summary (generated via OpenAI with `web_search_preview`) is written to a `.txt` file rather than an Excel sheet to avoid cell size limits.

### 8. Cross-platform file open
Both exporters use `platform.system()` to choose between `os.startfile()` (Windows) and `subprocess.run(["open", ...])` (Mac).

### 9. No EDGAR, no FRED in V1
DCF, WACC, and XBRL parsing are V2 features.

---

## Development Workflow

Each phase follows a 9-step sequence:

1. **Requirements** — What does this module need to do? Edge cases?
2. **Architecture** — Where does it live? What does it call/return?
3. **Pseudocode** — Write logic in plain English before touching code
4. **Scaffold** — Create file with docstring + `pass`-body stubs
5. **Draft** — Implement the code
6. **Review** — Review for correctness, edge cases, style
7. **Fix** — Correct all flagged issues
8. **Verify** — Run the code; confirm it works
9. **Sign-off** — Approve; update `docs/RFC.md`; move to next phase

---

## Current Position

**Phase 15 — COMPLETE. Next: Phase 16 — Caching Layer**

Phase 14 (`workflows/company_info.py`) fully signed off:
- `run()` — end-to-end V1 flow: company search → confirmation → period selection → fetch → parse → export
- Outer loop: "analyze another company?" after each export
- Inner loop: company name → OpenAI resolution → confirmation
- `CompanyResolverError` → show message → go to "analyze another?" prompt
- Period capped at 4 years / 4 quarters
- AI summary exported as `.txt` via `exporters/ai_summary_exporter.py`
- Both files auto-open after export (cross-platform)
- `main.py` simplified to splash + `run()` call

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
| 10 | ✅ Complete | Data Parsers |
| 11 | ✅ Complete | Period Selection UI |
| 12 | ✅ Complete | Excel Exporter |
| 13 | ✅ Complete | AI Summary |
| 14 | ✅ Complete | Company Report Workflow |
| 15 | ✅ Complete | Documentation |
| 16 | ⬜ | Caching Layer |
| 17 | ⬜ | Error Handling + Polish |
| 18 | ⬜ | Unit Tests |
| 19 | ⬜ | Integration Tests |
