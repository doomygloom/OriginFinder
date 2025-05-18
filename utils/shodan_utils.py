import shodan
from config import SHODAN_API_KEY

def get_shodan_ips(domain):
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        results = api.search(f'hostname:"{domain}"')
        return list(set([item['ip_str'] for item in results['matches']]))
    except Exception:
        return []
