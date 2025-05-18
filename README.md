# OriginFinder

Identify the origin IP address of a domain behind a CDN using subdomain enumeration, DNS lookups, and Shodan historical data.

* DNS and CDN IP Detection: Identifies IP addresses associated with a domain via DNS lookups.
* Subdomain Enumeration: Gathers subdomains using `crt.sh` data.
* Shodan Historical IP Analysis: Fetches potential origin IPs using Shodan API.
* Content Comparison: Identifies origin IPs by comparing HTTP response content with the main domain.
* CDN Header Detection: Flags missing CDN headers to indicate potential origin exposure.

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/doomygloom/OriginFinder.git
   cd OriginFinder
   ```

2. **Install required packages:**

   ```bash
   pip install requests tldextract
   ```

3. **Add your Shodan key to `config.py`**
   
---

## Usage

```bash
python OriginFinder.py <domain>
```

### Example:

1. Check a domain for origin exposure:

   ```bash
   python OriginFinder.py example.com
   ```

---

## Output

* **CDN IPs:** IPs associated with the domain's CDN.
* **Subdomains:** Detected subdomains via crt.sh.
* **Historical IPs:** Potential origin IPs from Shodan data.
* **Origin IP Analysis:** Identifies potential origin IPs by content comparison.
* **CDN Header Analysis:** Flags missing CDN headers to indicate direct origin exposure.
