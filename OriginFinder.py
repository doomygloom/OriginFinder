import sys
from utils.dns_utils import get_dns_ips
from utils.shodan_utils import get_shodan_ips
from utils.http_utils import compare_content
import tldextract
import requests

# X: @owldecoy

def get_subdomains(domain):
    parsed = tldextract.extract(domain)
    root = f"{parsed.domain}.{parsed.suffix}"
    try:
        r = requests.get(f"https://crt.sh/?q=%25.{root}&output=json", timeout=10)
        entries = {item['name_value'] for item in r.json()}
        return sorted(set(s for e in entries for s in e.split('\n') if root in s))
    except:
        return []

def main(domain):
    print(f"[+] Scanning: {domain}")
    
    cdn_ips = get_dns_ips(domain)
    print(f"[-] CDN IPs: {cdn_ips}")

    subdomains = get_subdomains(domain)
    print(f"[-] Found {len(subdomains)} subdomains")

    shodan_ips = get_shodan_ips(domain)
    print(f"[-] Shodan returned {len(shodan_ips)} historical IPs")

    candidates = list(set(shodan_ips) - set(cdn_ips))

    print("[*] Checking candidate IPs for origin match...")
    for ip in candidates:
        print(f"  -> Testing {ip} ...")
        match, missing = compare_content(domain, ip)
        if match:
            print(f"     [!] Potentially exposed origin: {ip}")
            print(f"     [-] Missing CDN headers: {missing}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python OriginFinder.py <domain>")
        sys.exit(1)
    main(sys.argv[1])
