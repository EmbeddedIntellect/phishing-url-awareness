Phishing URL Awareness Checker

1. Project Overview
The Phishing URL Awareness Checker is a beginner-friendly Python project that identifies common warning signs in URLs that may be associated with phishing.

It examines URL text only. It does not visit websites or send data over the internet.

2. Features
The program checks for six warning signs:
- Presence of the `@` symbol
- URL length greater than 100 characters
- IPv4-looking hostname
- Five or more hostname labels
- Punycode marker (`xn--`)
- Use of HTTP instead of HTTPS

It also displays explanations of detected warning signs.

3. Requirements
- Python 3.10 or later
- No external Python packages required

4. How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

   `python phishing_checker.py`

4. Enter a URL when prompted.
5. Type `quit` to exit.

5. Example Output
The program displays the URL being checked and any warning signs it detects.

6. Testing
The project includes five sample URLs in `tests/test_samples.md`.

7. Screenshots
The `screenshots` folder contains:
- `sample_run.png`
- `test_results.png`

8. Improvements
- Interactive URL checking
- Explanations for warning signs
- Handling of malformed URL input
- Clearer results

9. Limitations
This tool checks only selected URL patterns. It cannot confirm whether a URL is safe or malicious.

No detected warning signs does not guarantee that a URL is safe.

10. Ethical Use
This project is intended for cybersecurity awareness and educational purposes only. It does not scan websites, visit URLs, or transmit data.

11. Author
Chavan Divya