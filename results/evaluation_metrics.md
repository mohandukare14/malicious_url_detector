# Model Training & Evaluation Report

- **Task:** Zero-Day Phishing & Malicious URL Classification
- **Dataset Size:** 1500 URLs (Balanced: 50% Benign, 50% Malicious)
- **Train/Test Split:** 80% / 20% Stratified

## 1. Comparative Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression (Baseline)** | 99.67% | 99.34% | 100.00% | 0.9967 | 1.0000 |
| **Random Forest Classifier (Ensemble)** | **99.67%** | **100.00%** | **99.33%** | **0.9967** | **1.0000** |

## 2. Confusion Matrix (Random Forest)

- True Negatives (Correctly Identified Benign): **150**
- False Positives (Benign misclassified as Malicious): **0**
- False Negatives (Malicious missed): **1**
- True Positives (Correctly Flagged Attacks): **149**

## 3. Top Feature Importances

- `count_questions`: 23.44%
- `keyword_hits`: 22.97%
- `count_equals`: 13.29%
- `url_length`: 11.23%
- `url_entropy`: 10.94%
- `path_length`: 3.93%
- `domain_length`: 3.72%
- `digit_ratio`: 3.20%
