import re
import math
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = [
    "login", "signin", "verify", "verification", "secure", "security",
    "account", "update", "banking", "bank", "wallet", "confirm", "confirmation",
    "password", "credential", "auth", "token", "recover", "ebayisapi",
    "webscr", "pay", "paypal", "appleid", "support", "billing", "checkpoint"
]

SHORTENER_DOMAINS = {
    "bit.ly", "tinyurl.com", "goo.gl", "ow.ly", "t.co", "is.gd",
    "buff.ly", "adf.ly", "bit.do", "cutt.ly"
}

def calculate_entropy(text: str) -> float:
    """Calculates the Shannon entropy of a string to detect randomness/obfuscation."""
    if not text:
        return 0.0
    entropy = 0.0
    length = len(text)
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def extract_url_features(url: str) -> dict:
    """
    Extracts 19 lexical, structural, and statistical features from a URL.
    Handles bare domains (e.g. 'youtube.com') as well as full URLs.
    """
    raw_url = str(url).strip()
    
    # Check explicit protocol presence
    has_explicit_https = 1 if raw_url.lower().startswith('https://') else 0
    has_explicit_http = 1 if raw_url.lower().startswith('http://') else 0

    if not (has_explicit_https or has_explicit_http):
        # Bare domain or path without scheme (e.g., 'youtube.com/watch')
        parse_target = 'https://' + raw_url
        is_https = 1 # Modern web standard assumes HTTPS for bare domain lookups
    else:
        parse_target = raw_url
        is_https = has_explicit_https

    try:
        parsed = urlparse(parse_target)
        hostname = (parsed.hostname or "").lower()
        path = parsed.path or ""
        query = parsed.query or ""
    except Exception:
        hostname = raw_url.split('/')[0].lower()
        path = ""
        query = ""

    url_clean = raw_url
    url_length = len(url_clean)
    domain_length = len(hostname)
    path_length = len(path)

    # Delimiter and punctuation counts
    count_dots = url_clean.count('.')
    count_hyphens = url_clean.count('-')
    count_underscores = url_clean.count('_')
    count_slashes = url_clean.count('/')
    count_questions = url_clean.count('?')
    count_equals = url_clean.count('=')
    count_at = url_clean.count('@')
    count_ampersand = url_clean.count('&')

    # Numeric properties
    digits_count = sum(c.isdigit() for c in url_clean)
    digit_ratio = round(digits_count / url_length, 4) if url_length > 0 else 0.0

    # IPv4 Pattern check
    ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    has_ip = 1 if re.match(ip_pattern, hostname) else 0

    # Shannon Entropy
    domain_entropy = calculate_entropy(hostname)
    url_entropy = calculate_entropy(url_clean)

    # Subdomain count (e.g., www.youtube.com -> subdomain 'www' -> 1)
    subdomains = [s for s in hostname.split('.') if s]
    if len(subdomains) <= 2:
        subdomain_count = 0
    else:
        # e.g., 'www.google.com' has 3 parts -> 1 subdomain ('www')
        # 'paypal.com.verify-login.xyz' has 4 parts -> 2 subdomains
        subdomain_count = len(subdomains) - 2

    # Sensitive Keyword Hits
    url_lower = url_clean.lower()
    keyword_hits = sum(1 for kw in SUSPICIOUS_KEYWORDS if kw in url_lower)

    # Shortener check
    is_shortener = 1 if hostname in SHORTENER_DOMAINS else 0

    return {
        "url_length": url_length,
        "domain_length": domain_length,
        "path_length": path_length,
        "count_dots": count_dots,
        "count_hyphens": count_hyphens,
        "count_underscores": count_underscores,
        "count_slashes": count_slashes,
        "count_questions": count_questions,
        "count_equals": count_equals,
        "count_at": count_at,
        "count_ampersand": count_ampersand,
        "digit_ratio": digit_ratio,
        "has_ip": has_ip,
        "domain_entropy": domain_entropy,
        "url_entropy": url_entropy,
        "subdomain_count": subdomain_count,
        "keyword_hits": keyword_hits,
        "is_https": is_https,
        "is_shortener": is_shortener
    }
