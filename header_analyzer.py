import requests

def scan(url):
    print("\n🔍 Checking HTTP Headers...")
    results = []
    try:
        response = requests.get(url)
        headers = response.headers

        if "Content-Security-Policy" not in headers:
            results.append({
                "type": "Missing CSP Header",
                "url": url,
                "severity": "Low",
                "description": "Content-Security-Policy header not found.",
                "suggestion": "Add CSP header to mitigate XSS and injection attacks."
            })
    except Exception:
        pass
    return results
