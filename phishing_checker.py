"""
Phishing URL Awareness Checker
A beginner-friendly, defensive tool that reviews URL text for warning signs.

Safety: This program does NOT visit URLs, make internet requests, scan websites,
or send data anywhere. It only examines the text entered by the user.
"""

from urllib.parse import urlparse
import re


def inspect_url(raw_url):
    """Return a list of warning messages found in the supplied URL text."""
    warnings = []

    if not isinstance(raw_url, str) or not raw_url.strip():
        raise ValueError("Please enter a URL.")

    raw_url = raw_url.strip()

    # urlparse can raise ValueError for malformed bracketed hostnames.
    try:
        parsed = urlparse(raw_url)
        hostname = parsed.hostname or ""
    except ValueError as error:
        raise ValueError(f"Could not parse this URL: {error}") from error

    if "@" in raw_url:
        warnings.append(
            "The URL contains '@'. This can make the actual destination harder to notice."
        )

    if len(raw_url) > 100:
        warnings.append(
            f"The URL is longer than 100 characters ({len(raw_url)} characters)."
        )

    # Check whether the hostname looks like an IPv4 address.
    ipv4_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    if re.fullmatch(ipv4_pattern, hostname):
        warnings.append(
            "The hostname looks like an IPv4 address instead of a regular domain name."
        )

    if hostname and len(hostname.split(".")) >= 5:
        warnings.append(
            "The hostname has 5 or more dot-separated parts."
        )

    if "xn--" in hostname.lower():
        warnings.append(
            "The hostname contains 'xn--', a marker used in internationalized domain names."
        )

    if parsed.scheme.lower() == "http":
        warnings.append(
            "The URL uses HTTP rather than HTTPS, so the connection is not protected by TLS."
        )

    return warnings


def main():
    """Run the interactive command-line checker."""
    print("=" * 58)
    print("          PHISHING URL AWARENESS CHECKER")
    print("=" * 58)
    print("This tool checks URL text only. It never opens or visits a URL.")
    print("Enter 'quit' to exit.\n")

    while True:
        raw_url = input("Enter a URL to review: ").strip()

        if raw_url.lower() in {"quit", "q", "exit"}:
            print("Thank you for using the Phishing URL Awareness Checker.")
            break

        try:
            warnings = inspect_url(raw_url)
        except ValueError as error:
            print(f"\nInput error: {error}\n")
            continue

        print("\nReview results:")
        if warnings:
            for number, warning in enumerate(warnings, start=1):
                print(f"  {number}. {warning}")
            print("\nSummary: Review carefully. One or more warning signs were found.")
        else:
            print("  No listed warning signs were detected.")
            print("Summary: No listed warning signs were detected.")

        print(
            "\nImportant: This result does NOT prove that a URL is safe. "
            "It only checks the warning signs listed in this project.\n"
        )


if __name__ == "__main__":
    main()
