import argparse
from utils import validate_url
from modules import sqli_scanner, xss_scanner, header_analyzer
from report_generator import generate_report
import datetime

def main():
    print("=======================================")
    print("🛡️  Niqat Al-Daef - Web Vulnerability Scanner")
    print("=======================================\n")

    target_url = input("Enter target URL (e.g., http://localhost/dvwa/): ")
    if not validate_url(target_url):
        print("❌ Invalid or unreachable URL. Exiting.")
        return

    print("\nSelect scan modules:")
    print("1. SQL Injection")
    print("2. Cross-Site Scripting (XSS)")
    print("3. Header Analyzer")
    print("4. Run all scans")

    choice = input("Enter choice (1-4): ")

    results = []
    start_time = datetime.datetime.now()

    if choice in ["1", "4"]:
        results.extend(sqli_scanner.scan(target_url))
    if choice in ["2", "4"]:
        results.extend(xss_scanner.scan(target_url))
    if choice in ["3", "4"]:
        results.extend(header_analyzer.scan(target_url))

    end_time = datetime.datetime.now()
    scan_time = (end_time - start_time).total_seconds()

    generate_report(target_url, results, scan_time)

if __name__ == "__main__":
    main()
