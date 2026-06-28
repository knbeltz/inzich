# Kai's Learning Notes

Personal notes on concepts encountered during the Inzich mentorship project.

---

## When to use a Class vs. a Function

**Short answer:** Use a class when you have **state** that needs to persist across multiple operations. Use a function when you just need to transform an input into an output.

**What is state?**
State is data that needs to be remembered between calls. In `YahooClient`, the state is `self.ticker` and `self._yf_ticker` — the yfinance Ticker object that gets created once and reused. If we used plain functions, we'd have to pass the ticker and recreate the yfinance object on every single call.

**The rule of thumb:**

| Situation | Use |
|---|---|
| You need to store data that multiple methods share | Class |
| You're wrapping an external resource (API client, DB connection) | Class |
| You need multiple methods that all operate on the same data | Class |
| You just need to take an input and return an output | Function |
| The logic is simple and self-contained | Function |

**Real examples from this project:**
- `YahooClient` → class, because it holds `self._yf_ticker` (state shared across methods)
- `ask_company_name()` in `ui/prompts.py` → function, because it just shows a prompt and returns a string — no state needed
- `show_main_menu()` in `ui/menus.py` → function, same reason

**Another way to think about it:**
If you find yourself passing the same variable into multiple functions over and over, that variable probably wants to be `self.something` on a class instead.

**Why specifically is `YahooClient` a class?**

Because `self._yf_ticker = yf.Ticker(self.ticker)` needs to be created once and reused. Creating a yfinance Ticker object isn't free — if `fetch_all()` were a plain function, it would have to recreate it on every call. The class stores it in `__init__` so all methods can share it.

The thinking order is:
1. "I need to store state that multiple methods share" → choose a class
2. "I'm using a class, so I need somewhere to set up that state" → write `__init__`

`__init__` doesn't force you to use a class — you chose the class first because you needed shared state. `__init__` is just the tool that makes the setup happen.

---

## More concepts to add...

*(Add new entries here as they come up in the project)*
