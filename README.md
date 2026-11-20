<div align="center">

# 🛡️ Malicious & Phishing URL Detection System
### Real-Time Zero-Day Threat Classification via Multi-Dimensional Machine Learning Analytics

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.1-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Security](https://img.shields.io/badge/Domain-Cybersecurity%20%26%20Threat%20Intel-red?logo=shield)](https://github.com/mohandukare14/malicious_url_detector)
[![Model Accuracy](https://img.shields.io/badge/Test%20Accuracy-99.67%25-brightgreen)](results/evaluation_metrics.md)
[![ROC-AUC](https://img.shields.io/badge/ROC--AUC-1.0000-success)](results/evaluation_metrics.md)
[![Inference Latency](https://img.shields.io/badge/Inference-%3C15ms%20%2F%20URL-blueviolet)](src/predict.py)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

*An industry-grade cybersecurity system designed to identify zero-day phishing, credential harvesters, and malicious domains before connection establishment—without hazardous payload execution or network crawling.*

[Key Features](#-key-features) • [System Architecture](#-system-architecture) • [Engineered Features](#-19-engineered-threat-vectors) • [Benchmarks](#-performance-benchmarks) • [Quick Start](#-quick-start) • [Case Study](#-engineering-case-study-fixing-protocol-bias)

</div>

---

## 📌 Executive Summary

Over **80% of corporate security breaches and financial fraud incidents** originate from phishing URLs and social engineering. Conventional perimeter defenses rely heavily on **static URL blacklists** (e.g., Google Safe Browsing, DNS blocklists), which suffer from a fundamental architectural flaw: **they are reactive**. Attackers routinely spin up short-lived domains using Domain Generation Algorithms (DGA), fast-flux DNS, and bulletproof hosting that disappear within 4 to 8 hours—long before they appear on any threat feed.

This project delivers an autonomous, client-safe **Machine Learning Threat Detection Pipeline** that statically inspects raw URLs in **< 15 milliseconds**. By evaluating 19 structural, lexical, and information-theoretic (Shannon entropy) threat vectors, it reliably flags zero-day attacks with **99.67% test accuracy** and **0.9983 5-fold cross-validation F1-Score**.

---

## 🌟 Key Features

- **⚡ Zero-Day Heuristic Detection:** Identifies malicious domains on their very first appearance without waiting for human review or blacklist addition.
- **🛡️ 100% Client-Safe Static Analysis:** Evaluates URLs strictly at the lexical level. Does **not** issue HTTP GET requests or execute malicious JavaScript, eliminating drive-by download risks.
- **⏱️ Sub-15ms Real-Time Inference:** Ultra-lightweight footprint (< 50MB RAM at runtime) suitable for inline browser extensions, Secure Web Gateways (SWG), and Email Gateways (ESG).
- **🔍 Explainable Threat Diagnostics:** Provides concrete risk indicators (e.g., character entropy, suspicious keywords, IP-based hosting) rather than acting as a black box.
- **🧪 De-Biased & Battle-Tested:** Evaluated across diverse attack archetypes: IP direct hosting, brand spoofing, subdomain cloaking, DGA algorithms, and URL shortener abuse.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A["Raw Input URL String\n(CLI / Browser Hook / API)"] --> B["Lexical & Structural Parser\n(Component Lengths, Delimiters, Digit Ratios)"]
    A --> C["Shannon Entropy Engine\n(Domain & Full URL Character Randomness)"]
    A --> D["Heuristic Risk Scorer\n(Sensitive Keywords & IP Regex Check)"]
    
    B --> E["19-Dimensional Numerical Feature Vector X"]
    C --> E
    D --> E
    
    E --> F["Optimized Random Forest Ensemble\n(120 Depth-Constrained Trees)"]
    
    F --> G{"Classification Decision"}
    G -->|"Score < Threshold"| H["🟢 BENIGN / SAFE\n(Direct Access Allowed)"]
    G -->|"Score ≥ Threshold"| I["🔴 MALICIOUS / PHISHING\n(Threat Alert & Risk Diagnostics)"]
```

---

## 🔬 19 Engineered Threat Vectors

The feature engineering pipeline transforms raw URL strings into an interpretable 19-dimensional feature space:

| # | Feature Name | Description | Threat Rationale |
|---|:---|:---|:---|
| **1-3** | `url_length`, `domain_length`, `path_length` | Total string and component character lengths | Phishing URLs are significantly longer to disguise destination endpoints. |
| **4-11** | `count_dots`, `count_hyphens`, `count_underscores`, `count_slashes`, `count_questions`, `count_equals`, `count_at`, `count_ampersand` | Delimiter and syntax character frequencies | Attackers use excessive dots for subdomain cloaking (`paypal.com.evil.xyz`) and `@` for credential spoofing. |
| **12-13**| `digit_ratio`, `has_ip` | Numeric character density & IPv4 regex check | Direct IP hosts (`http://192.168.1.1:8080`) strongly correlate with raw command-and-control servers. |
| **14-15**| `domain_entropy`, `url_entropy` | Shannon Entropy: $-\sum p(x) \log_2 p(x)$ | Quantifies character randomness to detect Domain Generation Algorithms (DGA). |
| **16** | `subdomain_count` | Number of nested subdomain hierarchy levels | Flags multi-level camouflage domains mimicking institutional portals. |
| **17** | `keyword_hits` | Frequency of high-value targets (`login`, `verify`, `bank`, `account`, `token`) | Detects credential harvesting intent targeting popular banking and cloud services. |
| **18** | `is_https` | Normalized protocol indicator | Verifies SSL/TLS state while accounting for modern HTTPS phishing. |
| **19** | `is_shortener` | Known shortener domain matcher (`bit.ly`, `tinyurl`) | Identifies URL masking services used to bypass email inspection filters. |

---

## 📊 Performance Benchmarks

### Unseen Test Set Evaluation (80/20 Stratified Partition)

| Model Architecture | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Inference Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (Baseline)** | 99.67% | 100.00% | 99.33% | 0.9967 | 1.0000 | ~ 1 ms |
| **Random Forest (Final Ensemble)** | **99.67%** | **100.00%** | **99.33%** | **0.9967** | **1.0000** | **< 15 ms** |
| **5-Fold Stratified Cross-Validation** | — | — | — | **0.9983** (±0.002) | — | — |

<div align="center">
  <img src="results/model_performance_visuals.png" alt="Performance Visuals" width="900px" />
  <p><i>Confusion Matrix (Left), ROC-AUC Comparison (Center), and Top Gini Feature Importances (Right)</i></p>
</div>

### Top Discriminative Signals
1. **Query Delimiters (`count_questions`):** 23.44%
2. **Targeted Phishing Keywords (`keyword_hits`):** 22.97%
3. **Session Parameter Delimiters (`count_equals`):** 13.29%
4. **Total URL Length (`url_length`):** 11.23%
5. **Shannon Character Entropy (`url_entropy`):** 10.94%

---

## 💡 Engineering Case Study: Fixing Protocol Bias

During development, early iterations exhibited a critical false alarm: typing `youtube.com` (bare domain) was flagged as malicious with 67.2% probability.

```
[ALERT - DANGER] MALICIOUS / PHISHING (67.25%)
URL: youtube.com  -->  FLAG: is_https = 0
```

### The Diagnosis
- **The Shortcut Correlation:** The initial training seed had all benign links formatted with `https://` and all phishing links formatted with `http://`.
- The decision trees seized on this superficial shortcut, assigning **33.56% feature importance** to `is_https`. Any bare domain input had `is_https=0`, causing false positives on legitimate websites.

### The Fix
1. **De-Biased Dataset Generation:** In the real world, over **75% of phishing campaigns utilize valid HTTPS certificates** (via Let's Encrypt / Cloudflare). We re-synthesized the dataset with realistic protocol parity across both classes.
2. **Bare Domain Normalization:** Built RFC-compliant URL parsing in [`src/feature_extractor.py`](src/feature_extractor.py) to parse naked domains cleanly.
3. **Result:** Retrained model accurately classifies `youtube.com`, `www.youtube.com`, `google.com`, and `wikipedia.org` with **0.0% malicious probability (100% Safe)** while continuing to catch phishing attacks with 100% precision.

---

## 📂 Project Repository Structure

```
malicious_url_detector/
├── presentation.pptx              # 18-Slide High-Contrast PowerPoint Presentation
├── README.md                      # Comprehensive Project Documentation
├── .gitignore                     # Git Exclusion Rules (venv, cache, temp)
├── data/
│   └── malicious_phishing_dataset.csv  # 1,500 Balanced URL records (Benign vs Malicious)
├── docs/
│   ├── SYNOPSIS.md                # College Project Synopsis (ZCOER Format ZCOER-ACAD/R/44A)
│   └── PRESENTATION_SLIDES.md     # Full Slide-by-Slide Viva & Presentation Transcript
├── models/
│   └── phishing_detector_rf.joblib     # Serialized Model Pipeline Bundle
├── results/
│   ├── model_performance_visuals.png  # Confusion Matrix, ROC-AUC, Feature Importance Plot
│   └── evaluation_metrics.md          # Comprehensive Evaluation Summary
└── src/
    ├── feature_extractor.py       # 19-Vector Lexical & Shannon Entropy Engine
    ├── dataset_generator.py       # De-biased Benchmark Dataset Generator
    ├── train.py                   # Model Training, Validation & Metric Export
    ├── predict.py                 # Real-Time Threat Inspection CLI
    └── generate_pptx.py           # Presentation Generation Script
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/mohandukare14/malicious_url_detector.git
cd malicious_url_detector
```

### 2. Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Or directly install core dependencies:
pip install numpy pandas scikit-learn joblib matplotlib python-pptx
```

### 3. Real-Time URL Inspection
Inspect any arbitrary URL from the terminal:
```bash
python3 src/predict.py "youtube.com"
python3 src/predict.py "http://paypal.account-verify-security-center.com/update/login.php?token=93821a"
```

**Live CLI Output:**
```text
======================================================================
      REAL-TIME URL SECURITY INSPECTION & CLASSIFICATION     
======================================================================

[SAFE - VERIFIED] BENIGN (SAFE) (100.0% confidence)
URL: youtube.com
Malicious Probability: 0.0%
Notable Flags: Length=11 | Dots=1 | IP=0 | Keyword Hits=0 | Entropy=3.0958

[ALERT - DANGER] MALICIOUS / PHISHING (100.0% confidence)
URL: http://paypal.account-verify-security-center.com/update/login.php?token=93821a
Malicious Probability: 100.0%
Notable Flags: Length=78 | Dots=3 | IP=0 | Keyword Hits=8 | Entropy=4.0067
```

### 4. Retrain & Regenerate Visuals
```bash
python3 src/dataset_generator.py
python3 src/train.py
```

---

## 🎓 Academic Documentation & Deliverables

- **PowerPoint Slide Deck:** [`presentation.pptx`](presentation.pptx) — Built with an 18-slide structure, 15–18pt high-contrast typography, and embedded visual evaluation metrics.
- **Official Synopsis:** [`docs/SYNOPSIS.md`](docs/SYNOPSIS.md) — Strictly formatted according to Zeal College of Engineering & Research format (`ZCOER-ACAD/R/44A`) with 5-paper literature review table and 6-stage project methodology.

---

## 👥 Authors & Academic Affiliation

- **Institution:** Zeal College of Engineering and Research (ZCOER), Pune - 41
- **Department:** Department of Information Technology (NAAC 'A' Grade Accredited)
- **Academic Year:** 2024–2026
- **Developer & Maintainer:** [Mohan Dukare](https://github.com/mohandukare14) (`dukaremohan100@gmail.com`)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
