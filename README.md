# Phishing URL Awareness Checker

## Overview
The Phishing URL Awareness Checker is a beginner-friendly Python command-line project. It reviews URL text for a small set of common warning signs to support cybersecurity awareness.

**Safety:** The program only examines text entered by the user. It does not visit URLs, scan websites, make internet requests, or send data anywhere.

## Features
The checker looks for these six warning signs:
1. The `@` symbol in the URL.
2. A URL longer than 100 characters.
3. A hostname that looks like an IPv4 address.
4. A hostname containing 5 or more dot-separated parts.
5. The `xn--` punycode marker in the hostname.
6. The HTTP scheme.

It also provides explanations, handles malformed input, and lets the user check multiple URLs until they choose to quit.

## Requirements
- Python 3.10 or later
- No third-party packages are required.

## How to Run
1. Open Command Prompt or a terminal.
2. Change directory to this project folder. For example:

   ```powershell
   cd Desktop\phishing-url-awareness
   ```

   If you saved the folder elsewhere, use its actual path.
3. Run:

   ```powershell
   python phishing_checker.py
   ```

4. Enter a URL string when prompted. Type `quit` to exit.

## Example Output

```text
Enter a URL to review: http://192.0.2.10/account

Review results:
  1. The hostname looks like an IPv4 address instead of a regular domain name.
  2. The URL uses HTTP rather than HTTPS, so the connection is not protected by TLS.

Summary: Review carefully. One or more warning signs were found.
```

## Testing
See `tests/test_samples.md` for the five safe sample strings and expected warning signs. You can run the checker manually using those samples.

## Screenshots
After running the program, save screenshots of:
- A sample program run as `screenshots/sample_run.png`
- Your test results as `screenshots/test_results.png`

These screenshot files are not included because they need to be captured from your own computer after you run the project.

## Improvements
- Added an interactive loop with a quit option.
- Added a summary message after each review.
- Added malformed-input handling.
- Added an explanation for each detected warning sign.

## Limitations
- This project uses only six simple text-based checks.
- It does not determine whether a URL is genuinely malicious.
- It does not follow redirects, inspect website content, or check reputation databases.
- A result with no listed warning signs is not proof that a URL is safe.

## Ethical Use
Use this tool for learning and defensive cybersecurity awareness. Do not use it to target, disrupt, or access systems without permission. Use only safe sample strings for demonstrations.

## Author
Add your name here.
