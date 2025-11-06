# 🧾 Known Issue Table

| Issue | Type | Line(s) | Description | Fix Approach |
|--------|------|----------|--------------|---------------|
| Mutable default argument | Bug | 12 | `logs=[]` shared across multiple calls, causing shared state between executions | Changed default to `None` and initialized inside the function |
| Missing module and function docstrings | Style | 1, 8, 14, 22, 25, 31, 36, 41, 48 | Functions and module lacked proper documentation | Added descriptive docstrings for the module and all functions |
| Invalid naming convention | Style | 8, 14, 22, 25, 31, 36, 41 | Function names like `addItem`, `removeItem`, `getQty` did not follow `snake_case` | Renamed all functions using Python naming style (`add_item`, `remove_item`, `get_qty`, etc.) |
| Bare `except:` usage | Bug | 19 | Caught all exceptions without specifying type or message | Replaced with `except Exception as error:` and added error message printing |
| Unused import | Minor | 2 | `logging` was imported but never used anywhere | Removed the unused `import logging` statement |
| Missing encoding and improper file handling | Quality | 26, 32 | Used `open()` without specifying encoding and without `with` block | Used `with open(..., encoding="utf-8")` to safely handle file I/O |
| Insecure use of `eval()` | Security | 59 | Used `eval()` for printing, which can execute arbitrary code | Removed `eval()` and replaced with a normal `print()` statement |
| No input validation | Logic | 8 | Function accepted invalid types like `int` for item and `str` for quantity | Added type checking to ensure `item` is a string and `qty` is an integer |
| Missing blank lines between functions | Style | 8–48 | Did not follow PEP8 formatting (2 blank lines between functions) | Added proper spacing between function definitions for readability |

---

✅ **Total Issues Fixed:** 9  
✅ **Tools Used:** Pylint, Flake8, Bandit  
✅ **Final Result:** Pylint score improved from **4.80 → 9.52/10**, with Flake8 and Bandit reports clean.
