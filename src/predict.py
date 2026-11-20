import os
import sys
import joblib
import pandas as pd

# Add current dir to import feature extractor
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from feature_extractor import extract_url_features

def load_detector():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(project_dir, "models", "phishing_detector_rf.joblib")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}. Run train.py first!")
    bundle = joblib.load(model_path)
    return bundle

def inspect_url(url: str, bundle=None):
    if bundle is None:
        bundle = load_detector()
    
    model = bundle["model"]
    feature_names = bundle["feature_names"]
    
    feats = extract_url_features(url)
    df_feats = pd.DataFrame([feats])[feature_names]
    
    pred = model.predict(df_feats)[0]
    prob = model.predict_proba(df_feats)[0]
    
    label_str = "MALICIOUS / PHISHING" if pred == 1 else "BENIGN (SAFE)"
    confidence = prob[1] if pred == 1 else prob[0]
    
    return {
        "url": url,
        "prediction": int(pred),
        "label": label_str,
        "confidence": round(float(confidence) * 100, 2),
        "phishing_probability": round(float(prob[1]) * 100, 2),
        "extracted_features": feats
    }

if __name__ == "__main__":
    test_urls = [
        "https://www.google.com/search?q=machine+learning+cybersecurity",
        "https://github.com/torvalds/linux",
        "http://paypal.account-verify-security-center.com/update/login.php?token=93821a",
        "http://192.168.1.105:8080/secure-login/appleid/verify.php",
        "http://chase.online-account-recovery-portal.com/auth/login.html",
        "https://scikit-learn.org/stable/modules/ensemble.html"
    ]
    
    if len(sys.argv) > 1:
        test_urls = [sys.argv[1]]
        
    print("=" * 70)
    print("      REAL-TIME URL SECURITY INSPECTION & CLASSIFICATION     ")
    print("=" * 70)
    
    bundle = load_detector()
    for u in test_urls:
        res = inspect_url(u, bundle)
        status_color = "[ALERT - DANGER]" if res["prediction"] == 1 else "[SAFE - VERIFIED]"
        print(f"\n{status_color} {res['label']} ({res['confidence']}% confidence)")
        print(f"URL: {res['url']}")
        print(f"Malicious Probability: {res['phishing_probability']}%")
        print(f"Notable Flags: Length={res['extracted_features']['url_length']} | "
              f"Dots={res['extracted_features']['count_dots']} | "
              f"IP={res['extracted_features']['has_ip']} | "
              f"Keyword Hits={res['extracted_features']['keyword_hits']} | "
              f"Entropy={res['extracted_features']['domain_entropy']}")
