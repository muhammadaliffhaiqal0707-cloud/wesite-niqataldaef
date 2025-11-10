import requests

def validate_url(url):
    if not url.startswith(("http://", "https://")):
        return False
    try:
        response = requests.get(url, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False
