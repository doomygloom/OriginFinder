import requests

def check_missing_cdn_headers(response):
    cdn_headers = [
        'CF-Connecting-IP', 'X-Forwarded-For', 'X-Akamai-Edgescape',
        'X-CDN', 'Via', 'X-Cache'
    ]
    return [h for h in cdn_headers if h not in response.headers]

def compare_content(domain, ip):
    try:
        headers = {'Host': domain}
        r1 = requests.get(f"http://{ip}", headers=headers, timeout=5)
        r2 = requests.get(f"http://{domain}", timeout=5)

        if r1.status_code == 200 and r2.status_code == 200:
            if r1.text[:200] == r2.text[:200]:
                missing = check_missing_cdn_headers(r1)
                if missing:
                    return True, missing
        return False, []
    except Exception:
        return False, []
