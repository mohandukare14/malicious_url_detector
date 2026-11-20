import os
import csv
import random
import sys

sys.path.append(os.path.dirname(__file__))
from feature_extractor import extract_url_features

# Curated high-relevance representative URL seeds
BENIGN_SEEDS = [
    # Clean bare domains & www
    "youtube.com",
    "www.youtube.com",
    "https://www.youtube.com",
    "https://youtube.com",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "http://www.youtube.com/feed/trending",
    "google.com",
    "www.google.com",
    "https://www.google.com/search?q=machine+learning+tutorial",
    "github.com",
    "www.github.com",
    "https://github.com/torvalds/linux/commit/123456789abcdef",
    "wikipedia.org",
    "https://en.wikipedia.org/wiki/Cybersecurity",
    "stackoverflow.com",
    "https://stackoverflow.com/questions/1234567/python-string-parsing",
    "amazon.com",
    "https://www.amazon.com/dp/B08N5WRWNW/ref=hp_mod",
    "https://aws.amazon.com/documentation/s3/quickstart",
    "docs.python.org",
    "https://docs.python.org/3/library/urllib.parse.html",
    "mit.edu",
    "https://www.mit.edu/research/cybersecurity-lab",
    "stanford.edu",
    "https://www.stanford.edu/academics/departments",
    "nytimes.com",
    "https://www.nytimes.com/2026/05/12/technology/ai-advances.html",
    "cnn.com",
    "https://edition.cnn.com/world/europe/live-news-updates",
    "bbc.com",
    "https://www.bbc.com/news/technology-684210",
    "http://www.bbc.co.uk/programmes",
    "scikit-learn.org",
    "https://scikit-learn.org/stable/modules/ensemble.html",
    "kaggle.com",
    "https://www.kaggle.com/datasets/crawford/emnist",
    "huggingface.co",
    "https://huggingface.co/models?pipeline_tag=text-classification",
    "reddit.com",
    "https://www.reddit.com/r/MachineLearning/comments/xyz123/",
    "medium.com",
    "https://medium.com/@author/understanding-cyber-threats-2026",
    "arxiv.org",
    "https://arxiv.org/abs/2401.09876",
    "linkedin.com",
    "https://www.linkedin.com/in/engineering-manager-profile",
    "microsoft.com",
    "https://www.microsoft.com/en-us/security/business",
    "cloudflare.com",
    "https://cloudflare.com/learning/security/threats/zero-day-exploit/",
    "apple.com",
    "https://www.apple.com/shop/buy-iphone/iphone-16-pro",
    "developer.mozilla.org",
    "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers",
    "coursera.org",
    "https://www.coursera.org/learn/machine-learning-specialization",
    "netflix.com",
    "https://www.netflix.com/browse/genre/839338",
    "spotify.com",
    "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
]

PHISHING_SEEDS = [
    # Note: Modern phishing heavily uses HTTPS certificates (Let's Encrypt / Cloudflare)
    "https://paypal.account-verify-security-center.com/update/login.php?token=93821a",
    "http://paypal.account-verify-security-center.com/update/login.php?token=93821a",
    "https://appleid.apple.com.manage-login-credentials.info/auth/verify?id=9872",
    "http://appleid.apple.com.manage-login-credentials.info/auth/verify?id=9872",
    "https://bankofamerica.secure-session-validation.net/signon/login.action",
    "http://chase.online-account-recovery-portal.com/auth/login.html?session=8932",
    "https://chase.online-account-recovery-portal.com/auth/login.html?session=8932",
    "https://wellsfargo.customer-support-alert.org/confirmation/verify-identity",
    "https://amazon.shipping-delivery-failed-update.top/account/signin.php",
    "http://netflix-billing-update-subscription.xyz/login/payment-update",
    "https://netflix-billing-update-subscription.xyz/login/payment-update",
    "https://secure-microsoft-office365-verify-portal.club/auth/login?email=user",
    "http://google-drive-shared-confidential-doc.link/doc/view.php?auth=true",
    "https://facebook-security-infraction-appeal.support/login.php?checkpoint=1",
    "https://instagram-copyright-infringement-ticket.site/verify-badge/login",
    "https://coinbase-wallet-security-recovery.biz/wallet/phrase-confirm.php",
    "https://metamask-security-vault-sync.info/connect/seed-phrase-verify",
    "https://binance-security-kyc-update.top/user/login-2fa-bypass.html",
    "http://192.168.1.105:8080/secure-login/paypal.com/webscr.php?cmd=_login-run",
    "http://172.16.254.1:3000/auth/login-credential-harvester.php?ref=mail",
    "http://10.0.0.15/verification/bank-account/confirm.html",
    "https://dhl-express-parcel-tracking-redelivery.cc/tracking/reschedule?id=982",
    "https://fedex-package-customs-fee-notice.work/shipment/confirm-payment",
    "https://usps-address-confirmation-redeliver.top/redelivery/step1.php",
    "http://ebayisapi-dll-signin-account-verify.online/ebay/signin.aspx",
    "https://secure-login-citi-bank-alert.vip/portal/logon?auth_token=84732",
    "https://irs-tax-refund-claim-portal.gov-fake.org/refund/claim?case=78921",
    "https://verify-whatsapp-web-connection.tech/sync/qr-code-login.php",
    "http://bit.ly/3x89aZq-secure-login-verify-account",
    "http://tinyurl.com/bank-security-confirmation-update-profile",
    "https://dropbox-shared-urgent-invoice.online/view/invoice-download.php",
    "https://adobe-sign-secure-document-view.top/pdf/sign-in-prompt.php",
    "https://att-yahoo-mail-quota-exceeded-fix.net/login/update-mailbox.cgi"
]

def generate_variations(seeds, is_phishing=False, target_count=750):
    results = list(seeds)
    
    benign_domains = [
        "youtube.com", "google.com", "wikipedia.org", "github.com", "stackoverflow.com",
        "nytimes.com", "bbc.co.uk", "mit.edu", "stanford.edu", "aws.amazon.com",
        "medium.com", "kaggle.com", "scikit-learn.org", "python.org", "nature.com",
        "springer.com", "ieee.org", "bloomberg.com", "forbes.com", "ibm.com", "oracle.com",
        "mozilla.org", "w3schools.com", "zoom.us", "dropbox.com", "salesforce.com"
    ]
    benign_paths = [
        "", "watch?v=kYI98aZ", "channel/UCxyz", "feed/subscriptions", "articles/2026/01/overview",
        "docs/api/v2/reference", "courses/cs101/lecture1", "products/electronics/item-98214",
        "news/global/markets-update", "research/paper/download", "forum/threads/discussion-topic",
        "help/center/faq", "blog/engineering-insights", "about/company-team"
    ]
    
    phish_subdomains = ["login", "secure", "verify", "update-account", "portal", "webscr", "auth", "billing"]
    phish_brands = ["paypal", "appleid", "chase", "netflix", "amazon", "microsoft", "google", "bankofamerica", "coinbase"]
    phish_tlds = [".top", ".xyz", ".club", ".info", ".site", ".biz", ".cc", ".work", ".ru", ".link"]
    phish_actions = ["signin.php", "verify.html", "checkpoint.cgi", "login.action", "wallet-sync.php", "confirm-id.php", "auth.php"]

    random.seed(42)

    while len(results) < target_count:
        if not is_phishing:
            dom = random.choice(benign_domains)
            path = random.choice(benign_paths)
            style = random.choice(["https", "https_www", "bare", "www", "http"])
            
            p_part = f"/{path}" if path else ""
            if style == "https":
                url = f"https://{dom}{p_part}"
            elif style == "https_www":
                url = f"https://www.{dom}{p_part}"
            elif style == "bare":
                url = f"{dom}{p_part}"
            elif style == "www":
                url = f"www.{dom}{p_part}"
            else:
                url = f"http://{dom}{p_part}"
            results.append(url)
        else:
            style = random.choice(["ip", "subdomain_spoof", "tld_abuse", "shortener", "dga"])
            # In modern phishing, ~75% use HTTPS!
            protocol = random.choice(["https://", "https://", "https://", "http://"])
            
            if style == "ip":
                ip = f"{random.randint(11, 220)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"
                port = random.choice([8080, 80, 443, 8888, 3000])
                url = f"http://{ip}:{port}/{random.choice(phish_subdomains)}/{random.choice(phish_brands)}/{random.choice(phish_actions)}?token={random.randint(1000,99999)}"
            elif style == "subdomain_spoof":
                brand = random.choice(phish_brands)
                sub = random.choice(phish_subdomains)
                evil_dom = f"{brand}.{sub}-security-check{random.choice(phish_tlds)}"
                url = f"{protocol}{evil_dom}/auth/login.php?client_id={random.randint(10000,99999)}"
            elif style == "tld_abuse":
                brand = random.choice(phish_brands)
                tld = random.choice(phish_tlds)
                url = f"{protocol}{brand}-customer-service-resolution{tld}/{random.choice(phish_actions)}?session={random.randint(1000,9999)}"
            elif style == "shortener":
                shortener = random.choice(["bit.ly", "tinyurl.com", "is.gd", "cutt.ly"])
                slug = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=7))
                url = f"http://{shortener}/{slug}?redirect_to={random.choice(phish_brands)}-login"
            else: # DGA / Random high entropy
                dga = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(12, 22)))
                url = f"{protocol}{dga}.info/{random.choice(phish_actions)}?user={random.randint(100, 999)}"
            results.append(url)

    return results[:target_count]

def create_dataset(output_path: str, count_per_class: int = 750):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    benign_urls = generate_variations(BENIGN_SEEDS, is_phishing=False, target_count=count_per_class)
    phish_urls = generate_variations(PHISHING_SEEDS, is_phishing=True, target_count=count_per_class)
    
    all_data = []
    for u in benign_urls:
        all_data.append((u, 0)) # 0 = Benign
    for u in phish_urls:
        all_data.append((u, 1)) # 1 = Malicious/Phishing

    random.seed(42)
    random.shuffle(all_data)

    print(f"[*] Extracting features for {len(all_data)} balanced, de-biased URLs...")
    rows = []
    feature_names = None
    for url, label in all_data:
        feats = extract_url_features(url)
        if feature_names is None:
            feature_names = list(feats.keys())
        feats["url"] = url
        feats["label"] = label
        rows.append(feats)

    fieldnames = ["url"] + feature_names + ["label"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[+] Dataset created at {output_path} with {len(rows)} samples ({count_per_class} Benign, {count_per_class} Malicious).")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "malicious_phishing_dataset.csv")
    create_dataset(out)
