import dns.resolver

def get_dns_ips(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [ip.address for ip in answers]
    except:
        return []
