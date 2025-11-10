import requests

def scan(url):
    print("\n🔍 Scanning for SQL Injection...")
    payloads = ["' OR '1'='1", "';--", "\" OR \"1\"=\"1"]
    results = []
    for payload in payloads:
        try:
            response = requests.get(url + "?id=" + payload)
            if "mysql" in response.text.lower() or "syntax" in response.text.lower():
                results.append({
                    "type": "SQL Injection",
                    "url": url,
                    "parameter": "id",
                    "severity": "High",
                    "description": "Potential SQL injection vulnerability detected.",
                    "suggestion": "Use parameterized queries or prepared statements."
                })
                break
        except Exception:
            pass
    return results
