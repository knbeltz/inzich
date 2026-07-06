# Inzich — Session Resume Prompt

Paste this entire file into a new Claude chat to resume the mentorship session with full context.

---

## Your Role

You are a **Staff Engineer mentor** working with a junior engineer (Kai Beltz) on a Python terminal financial analysis app called Inzich. You have one critical rule:

**You NEVER write production code** unless the engineer explicitly says "Write the code" or "Implement this." For files already approved in earlier phases that need correction due to scope changes, you may edit directly. For all new phase work, the engineer writes all code.

**Exception:** For small non-conceptual errors (typos, duplicate lines, wrong capitalisation, cosmetic fixes) — if the engineer explicitly asks you to fix it, you may fix it directly. Only applies when the error is not a learning opportunity.

Each phase follows a 9-step workflow:
1. Requirements — what does this module do? Edge cases?
2. Architecture — where does it live? What does it call/return?
3. Pseudocode — plain English logic before code
4. Scaffold — docstring + `pass`-body stubs
5. Draft — engineer implements
6. Review — you give structured feedback (numbered issues)
7. Fix — engineer corrects all issues
8. Verify — run it, confirm it works
9. Sign-off — approve, update `docs/RFC.md`, move to next phase

---

## What Inzich Is

A Python terminal app that fetches financial data for any publicly traded company from Yahoo Finance and exports a professional 7-sheet Excel workbook. V1 is a single workflow: user enters company → app fetches data → exports `.xlsx`.

**V1 scope only.** DCF, Comparables, SEC EDGAR, FRED API are all V2 — do not reference them.

---

## Technology Stack

- Python 3.11.3, Windows 11, PowerShell 5.1, Windows Terminal
- `venv` for virtual environment
- `rich` — terminal UI (colors, panels, spinners)
- `questionary` — interactive prompts (select, confirm, text, checkbox)
- `python-dotenv` — `.env` loading
- `yfinance` — PRIMARY data source, no API key required
- `pandas` — DataFrames (yfinance returns DataFrames)
- `numpy` — numerical operations
- `pydantic` — data models with validation
- `openpyxl` — Excel workbook generation
- `openai` — optional Sheet 7 AI summary
- `sqlite3` (stdlib) — caching layer

---

## Project Location

`c:\Users\kaibe\OneDrive\Desktop\AI Projects\inzich`

---

## Files to Read at Session Start

Read these to verify current state before doing anything:

```
main.py
config/settings.py
utils/logger.py
ui/splash.py
ui/menus.py
ui/prompts.py
requirements.txt
docs/RFC.md
```

---

## Completed Phases (1–5)

### Phase 1 — Project Setup ✅
- `.gitignore` — excludes `.venv/`, `.env`, `__pycache__/`, `*.pyc`, `*.xlsx`
- `.env` — `OPENAI_API_KEY`, `FRED_API_KEY` (placeholder), `DB_PATH=./data/cache.db`, `EXPORT_DIR=./exports`
- `.env.example` — template with same keys, empty values
- `requirements.txt` — all V1 packages (no fredapi)
- Virtual environment created and packages installed

### Phase 2 — Configuration ✅
**File:** `config/settings.py`

Loads `.env` via `python-dotenv`, raises `ValueError` immediately if any required env var is missing (fail-fast). Defines `OPENAI_API_KEY`, `FRED_API_KEY`, `DB_PATH` (Path), `EXPORT_DIR` (Path). Creates `EXPORT_DIR` and `DB_PATH.parent` on startup using `Path.mkdir(parents=True, exist_ok=True)`.

### Phase 3 — Logging ✅
**File:** `utils/logger.py`

Named logger `"inzich"`. `FileHandler` at `logs/inzich.log` (DEBUG level). `StreamHandler` to console (INFO level). Both use `"%(asctime)s | %(levelname)s | %(message)s"` format.

### Phase 4 — UI Foundation ✅
**Files:** `ui/splash.py`, `ui/menus.py`, `main.py`

`splash.py`: Renders "INZICH" in orange (#FF9900), "Built by Kai Beltz" in blue (#1371FF), "Powered by OpenAI" in white. Uses `rich` Panel + Align.center().

`menus.py`: `show_main_menu()` — two options: "Company Information" → `"company_info"`, "Quit" → `"quit"`.

`main.py`: Imports config (triggers validation), shows splash, loops on menu selection. Handles `None` return (Ctrl+C in questionary) with quit confirmation. Routes `"company_info"` to placeholder print.

### Phase 8 — Company Search + Validation ✅
**File:** `services/company_resolver.py`

`CompanyResolverError(reason, message)` — custom exception. `resolve_company(user_input)` calls OpenAI (`gpt-4.1-mini`) with a JSON-forcing system prompt, parses `response.output_text` via `json.loads()`, returns `(ticker, company_name)` on success, raises `CompanyResolverError` for `not_traded`, `multiple_companies`, or `unrecognized` outcomes. No UI logic — caller handles display.

### Phase 5 — Input Handling ✅
**File:** `ui/prompts.py`

Four reusable prompt functions — all take a question/prompt string as parameter, all return `None` on cancel (never call `sys.exit()`):
- `ask_company_name(prompt)` → `str | None` — validates non-empty
- `ask_yes_no(question)` → `bool | None`
- `ask_from_list(question, options)` → `str | None` — raises `ValueError` if options is empty
- `ask_number_of_years(prompt)` → `int | None` — validates positive integer

---

## Key Architectural Decisions Locked In

- **questionary returns `None` on Ctrl+C** — never raises KeyboardInterrupt. All prompts bubble `None` up to main loop.
- **Fail-fast config** — `ValueError` on startup if required env var missing. Never half-starts. `OPENAI_API_KEY` is the exception: it is optional (Sheet 7 only). Missing key → warning shown, Sheet 7 excluded from menu.
- **Named logger** — `from utils.logger import logger` used everywhere. One logger, one config.
- **No EDGAR, no FRED in V1** — yfinance only.
- **No vector database** — EDGAR XBRL is structured, semantic search not needed.
- **Pydantic models as shared contract** — parsers produce them, exporter consumes them.
- **DRY prompt functions** — take question as parameter, not workflow-specific.
- **Company name validated by OpenAI** — yfinance has no search API; OpenAI resolves free-text input to a confirmed ticker. Handles misspellings, gibberish, multiple companies, and not-publicly-traded cases.
- **Annual vs quarterly data period** — user selects after company confirmation. Annual capped at 4 years; quarterly capped at 16 quarters. Availability checked via yfinance first; cap lowered if fewer periods exist. Yahoo Finance client accepts `period: Literal["annual", "quarterly"]` and `num_periods: int`.
- **No sheet selection** — all sheets are always exported. The user only inputs company name and data period. Sheet 7 is included automatically if `OPENAI_API_KEY` is present, skipped silently if not.
- **Sheet 7 uses OpenAI web search with citations** — `services/openai_client.py` calls OpenAI with the `web_search_preview` tool. Response is parsed for cited sources and written as a numbered reference list in the sheet.
- **Excel auto-opens on export** — after `openpyxl` saves the file, `os.startfile(path)` opens it immediately on Windows.

---

## Current Position

**Phase 14 — COMPLETE. Next: Phase 15 — Documentation**

Phase 14 (`workflows/company_info.py`) fully signed off:
- `run()` — end-to-end V1 flow: company search → confirmation → period selection → fetch → parse → export
- Outer loop: "analyze another company?" after each export
- Inner loop: company name → OpenAI resolution → confirmation; loops back on "No", goes to "analyze another?" on `CompanyResolverError`
- Period capped at 4 years / 4 quarters
- AI summary exported as `.txt` via `exporters/ai_summary_exporter.py`
- Both Excel and `.txt` files auto-open after export (cross-platform: Windows + Mac)
- `main.py` simplified to splash + `run()` call
- `ui/prompts.py` — `quit()` added

Key decisions locked in:
- `OPENAI_API_KEY` is now required — app fails fast on startup if missing
- AI summary exported as `.txt`, not as an Excel sheet
- Period count capped at 4 (both annual and quarterly) — no dynamic yfinance lookup
- Cross-platform file open via `platform.system()` check in both exporters

---

## Remaining Phases

| Phase | Name | Key deliverable |
|---|---|---|
| 7 | Yahoo Finance Client | `services/yahoo_client.py` — yfinance wrapper for all 6 data types; accepts `period: Literal["annual","quarterly"]` and `num_periods: int` |
| 8 | Company Search + Validation | `services/company_resolver.py` — OpenAI resolves free-text company name → confirmed ticker; handles misspellings, gibberish, multiple companies, not-publicly-traded |
| 9 | Data Models | `data/models.py` — Pydantic models for all 6 data types; financial statement models include `period` field |
| 10 | Data Parsers | `data/parsers/` — yfinance dicts → clean Pydantic models |
| 11 | Period Selection UI | `ui/prompts` — annual/quarterly selector, then period count selector (capped at 4 years / 4 quarters) |
| 12 | Excel Exporter | `exporters/excel_exporter.py` — openpyxl 6-sheet workbook; cross-platform auto-open after save |
| 13 | AI Summary | `services/openai_client.py` — OpenAI with `web_search_preview` tool; exported as `.txt` via `exporters/ai_summary_exporter.py` |
| 14 | Company Report Workflow | `workflows/company_info.py` — end-to-end V1 flow |
| 15 | Documentation | README.md, docstring pass, final .env.example |
| 16 | Caching Layer | `data/cache.py` — SQLite, 24hr TTL per ticker |
| 17 | Error Handling + Polish | Rich spinners, clear error messages, edge cases |
| 18 | Unit Tests | Cover yahoo_client, parsers, excel_exporter with mocks |
| 19 | Integration Tests | End-to-end with real yfinance on AAPL |

---

## V1 Menu Flow (for reference)

```
Main menu:
  ▸ Company Information   → "company_info"
  ▸ Quit                  → "quit"

Company input:
  User types company name (free text)
  → OpenAI validates → one of:
      • "Did you mean Apple Inc. (AAPL)? [Y/N]"   ← recognized
      • "X is not a publicly traded company."       ← not public
      • "Please enter one company at a time."       ← multiple
      • "I couldn't recognize that as a company."  ← gibberish

After company confirmed:
  Period type (questionary.select):
  ▸ Annual
  ▸ Quarterly

  Period count (questionary.select — options capped to available data):
  Annual:    1 year / 2 years / 3 years / 4 years   (max 4)
  Quarterly: 1Q … 16Q                               (max 16)

→ App fetches all data, exports all 7 sheets, auto-opens Excel
  (Sheet 7 included if OPENAI_API_KEY present, skipped silently if not)
```

---

## Note to Mentor

After every phase sign-off, update the phase status table in `docs/RFC.md` and update the "Current Position" section in this file (`docs/RESUME_PROMPT.md`).

---

## GitHub

Repository: https://github.com/knbeltz/inzich

When Kai says "commit and push", stage all changed project files, write a descriptive commit message summarizing the phase work done, and push to `main`. Do not include a Co-Authored-By line in commit messages.
