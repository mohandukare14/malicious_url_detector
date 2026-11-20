# Zero-Day Phishing & Malicious URL Classification Using Machine Learning Analytics

An industry-oriented cybersecurity mini-project that identifies malicious and phishing URLs in real time using 19 engineered lexical, structural, and Shannon entropy features.

---

## 📁 Project Structure

```
malicious_url_detector/
├── presentation.pptx              # Complete 18-slide PowerPoint presentation
├── README.md                      # Project documentation and guide
├── venv/                          # Python virtual environment symlink
├── data/
│   └── malicious_phishing_dataset.csv  # 1,200 Balanced URL records (Benign vs Malicious)
├── docs/
│   ├── SYNOPSIS.md                # Official college synopsis (ZCOER format ZCOER-ACAD/R/44A)
│   └── PRESENTATION_SLIDES.md     # Full slide transcript & content for presentation
├── models/
│   └── phishing_detector_rf.joblib     # Serialized Random Forest model bundle
├── results/
│   ├── model_performance_visuals.png  # Confusion Matrix, ROC Curves, Feature Importances
│   └── evaluation_metrics.md          # Comprehensive evaluation report
└── src/
    ├── feature_extractor.py       # 19-vector lexical & Shannon entropy engine
    ├── dataset_generator.py       # Benchmark dataset generator
    ├── train.py                   # Train/test split, model training & cross-validation
    ├── predict.py                 # Real-time URL threat inspection CLI
    └── generate_pptx.py           # PPTX generator script
```

---

## 🚀 How to Run the Project

Navigate to the project directory:
```bash
cd ~/Projects/malicious_url_detector
```

### 1. Test Real-Time URL Classification
Inspect any arbitrary URL with our trained model:
```bash
./venv/bin/python src/predict.py "http://paypal.account-verify-security-center.com/update/login.php"
```

### 2. Retrain the Model Pipeline
To regenerate the dataset, retrain models, and update evaluation graphs:
```bash
./venv/bin/python src/dataset_generator.py
./venv/bin/python src/train.py
```

### 3. Regenerate PowerPoint Presentation
```bash
./venv/bin/python src/generate_pptx.py
```

---

## 📊 Model Performance Highlights

- **Dataset Size:** 1,200 URLs (600 Benign, 600 Malicious)
- **Train/Test Partition:** 80% (960) / 20% (240) Stratified Split
- **Test Accuracy:** **100.0%**
- **Precision / Recall / F1-Score:** **1.0000**
- **5-Fold Stratified Cross-Validation Mean F1:** **99.90% (+/- 0.21%)**
- **Inference Latency:** **< 15ms per URL**
