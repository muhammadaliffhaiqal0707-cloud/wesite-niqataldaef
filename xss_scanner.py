import requests

def scan(url):
    print("\n🔍 Scanning for XSS...")
    payload = "<script>alert('XSS')</script>"
    results = []
    try:
        response = requests.get(url + "?msg=" + payload)
        if payload in response.text:
            results.append({
                "type": "Cross-Site Scripting (XSS)",
                "url": url,
                "parameter": "msg",
                "severity": "Medium",
                "description": "Reflected XSS detected in response output.",
                "suggestion": "Sanitize input and escape HTML output."
            })
    except Exception:
        pass
    return results
