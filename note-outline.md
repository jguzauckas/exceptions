# Exceptions

- Sample exception like dividebyzero
- Tracebacks to identify where errors come from (bottom to top)

- Python raises exceptions on its own, but we can raise them too
- `raise` statement
- Sample exception types:
    - IndexError, KeyError, NameError, OverflowError?, RuntimeError, StopIteration, TypeError, ValueError, ZeroDivisionError

- `try`, `except`(s), `else`\*, `finally`\*
- Catching more than one exception at once: `except(type1, type2) as e:`
    - Can also have more than one except for more granular raising