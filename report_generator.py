def generate_report(target_url, results, scan_time):
    print("\n=======================================")
    print("📋 SCAN REPORT - Niqat Al-Daef")
    print("=======================================\n")

    print(f"🌐 Target: {target_url}")
    print(f"⏱️ Scan Time: {scan_time:.2f} seconds")
    print("---------------------------------------")

    if not results:
        print("✅ No vulnerabilities detected!")
    else:
        for i, result in enumerate(results, start=1):
            print(f"\n[{i}] {result['type']}")
            for key, value in result.items():
                if key not in ['type']:
                    print(f"- {key.capitalize()}: {value}")

    print("\n=======================================")
    print("🛡️ Scan Completed. For educational use only.")
    print("=======================================")
