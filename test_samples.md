# Test Samples and Expected Results

These are the five safe sample strings from the project workbook. They are examples for text-only inspection; the program does not open or visit them.

| No. | Sample URL text | Expected warning sign(s) |
|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs |
| 2 | `http://192.0.2.10/account` | IPv4-looking hostname; HTTP scheme |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol; HTTP scheme |
| 4 | `https://a.b.c.d.e.example.invalid/path` | 5 or more hostname parts |
| 5 | `https://xn--example.invalid/` | `xn--` marker |

## How to Test
1. Run `python phishing_checker.py`.
2. Enter each sample string exactly as shown.
3. Compare the program's output with the expected warning signs above.
4. Type `quit` to exit.

## Notes
- The first sample is not guaranteed safe; it simply has none of this project's six listed warning signs.
- The IPv4 sample uses the reserved documentation address `192.0.2.10`.
- These checks are educational indicators, not a definitive phishing detector.
