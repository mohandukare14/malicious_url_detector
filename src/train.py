import os
import sys
import json
import joblib
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report, roc_curve
)

def run_training_pipeline():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(project_dir, "data", "malicious_phishing_dataset.csv")
    models_dir = os.path.join(project_dir, "models")
    results_dir = os.path.join(project_dir, "results")
    
    os.makedirs(models_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    print("=" * 60)
    print("      CYBERSECURITY ML PIPELINE: MALICIOUS URL DETECTOR     ")
    print("=" * 60)

    # 1. Load Data
    print(f"\n[1] Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)
    print(f"    Total samples: {len(df)}")
    print(f"    Class distribution: {df['label'].value_counts().to_dict()} (0=Benign, 1=Malicious)")

    feature_cols = [c for c in df.columns if c not in ["url", "label"]]
    X = df[feature_cols]
    y = df["label"]

    print(f"    Engineered features ({len(feature_cols)}): {', '.join(feature_cols[:6])}...")

    # 2. Train-Test Split (80% Train, 20% Unseen Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\n[2] Data Partitioned:")
    print(f"    Training samples : {len(X_train)}")
    print(f"    Test samples     : {len(X_test)}")

    # 3. Model 1: Baseline Logistic Regression (Standardized)
    print("\n[3] Training Baseline Model: Logistic Regression...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    baseline_model = LogisticRegression(max_iter=1000, random_state=42)
    baseline_model.fit(X_train_scaled, y_train)
    y_pred_base = baseline_model.predict(X_test_scaled)
    y_prob_base = baseline_model.predict_proba(X_test_scaled)[:, 1]

    acc_base = accuracy_score(y_test, y_pred_base)
    f1_base = f1_score(y_test, y_pred_base)
    roc_base = roc_auc_score(y_test, y_prob_base)
    print(f"    Baseline Accuracy : {acc_base * 100:.2f}% | F1: {f1_base:.4f} | ROC-AUC: {roc_base:.4f}")

    # 4. Model 2: Advanced Ensemble Model (Random Forest)
    print("\n[4] Training Candidate Model: Random Forest Classifier...")
    rf_model = RandomForestClassifier(
        n_estimators=120,
        max_depth=12,
        min_samples_split=4,
        random_state=42,
        n_jobs=-1
    )

    # 5-Fold Stratified Cross-Validation on Training set
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(rf_model, X_train, y_train, cv=cv, scoring='f1')
    print(f"    5-Fold Stratified CV F1-Scores: {[round(s, 4) for s in cv_scores]}")
    print(f"    Mean CV F1-Score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

    # Fit on entire training set
    rf_model.fit(X_train, y_train)

    # 5. Evaluate on Unseen Test Set
    print("\n[5] Evaluating Final Random Forest Model on Unseen Test Data...")
    y_pred_rf = rf_model.predict(X_test)
    y_prob_rf = rf_model.predict_proba(X_test)[:, 1]

    acc_rf = accuracy_score(y_test, y_pred_rf)
    prec_rf = precision_score(y_test, y_pred_rf)
    rec_rf = recall_score(y_test, y_pred_rf)
    f1_rf = f1_score(y_test, y_pred_rf)
    roc_rf = roc_auc_score(y_test, y_prob_rf)
    cm_rf = confusion_matrix(y_test, y_pred_rf)

    print(f"    --------------------------------------------------")
    print(f"    Accuracy  : {acc_rf * 100:.2f}%")
    print(f"    Precision : {prec_rf * 100:.2f}%")
    print(f"    Recall    : {rec_rf * 100:.2f}%")
    print(f"    F1-Score  : {f1_rf:.4f}")
    print(f"    ROC-AUC   : {roc_rf:.4f}")
    print(f"    Confusion Matrix:\n{cm_rf}")
    print(f"    --------------------------------------------------")

    # 6. Feature Importance Analysis
    importances = rf_model.feature_importances_
    sorted_idx = np.argsort(importances)[::-1]
    print("\n[6] Top 8 Most Discriminative URL Features:")
    top_features = []
    for rank, idx in enumerate(sorted_idx[:8], 1):
        feat_name = feature_cols[idx]
        feat_imp = importances[idx]
        top_features.append({"feature": feat_name, "importance": round(float(feat_imp), 4)})
        print(f"    {rank}. {feat_name:<20}: {feat_imp*100:.2f}%")

    # 7. Generate Visual Evaluation Plots
    plt.figure(figsize=(14, 5))

    # Plot A: Confusion Matrix
    plt.subplot(1, 3, 1)
    plt.imshow(cm_rf, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix (Test Set)', fontsize=12, fontweight='bold')
    plt.colorbar()
    tick_marks = np.arange(2)
    plt.xticks(tick_marks, ['Benign', 'Malicious'])
    plt.yticks(tick_marks, ['Benign', 'Malicious'])
    thresh = cm_rf.max() / 2.
    for i in range(cm_rf.shape[0]):
        for j in range(cm_rf.shape[1]):
            plt.text(j, i, format(cm_rf[i, j], 'd'),
                     ha="center", va="center",
                     color="white" if cm_rf[i, j] > thresh else "black",
                     fontsize=14, fontweight='bold')
    plt.ylabel('True Ground Truth')
    plt.xlabel('Predicted Label')

    # Plot B: ROC Curves (Baseline vs Random Forest)
    plt.subplot(1, 3, 2)
    fpr_base, tpr_base, _ = roc_curve(y_test, y_prob_base)
    fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
    plt.plot(fpr_base, tpr_base, label=f'Logistic Regression (AUC={roc_base:.3f})', linestyle='--')
    plt.plot(fpr_rf, tpr_rf, label=f'Random Forest (AUC={roc_rf:.3f})', color='darkgreen', linewidth=2)
    plt.plot([0, 1], [0, 1], 'k--', alpha=0.5)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve Comparison', fontsize=12, fontweight='bold')
    plt.legend(loc='lower right', fontsize=9)
    plt.grid(alpha=0.3)

    # Plot C: Top 8 Feature Importances
    plt.subplot(1, 3, 3)
    top_indices = sorted_idx[:8][::-1]
    plt.barh([feature_cols[i] for i in top_indices], [importances[i] for i in top_indices], color='teal')
    plt.title('Top 8 Feature Importances', fontsize=12, fontweight='bold')
    plt.xlabel('Gini Importance')
    plt.grid(axis='x', alpha=0.3)

    plt.tight_layout()
    plots_path = os.path.join(results_dir, "model_performance_visuals.png")
    plt.savefig(plots_path, dpi=200)
    plt.close()
    print(f"\n[7] Performance visuals saved to: {plots_path}")

    # 8. Save Trained Model Pipeline & Metadata
    model_artifact = {
        "model": rf_model,
        "feature_names": feature_cols,
        "metrics": {
            "accuracy": round(float(acc_rf), 4),
            "precision": round(float(prec_rf), 4),
            "recall": round(float(rec_rf), 4),
            "f1_score": round(float(f1_rf), 4),
            "roc_auc": round(float(roc_rf), 4),
            "cv_mean_f1": round(float(cv_scores.mean()), 4)
        },
        "top_features": top_features
    }
    model_save_path = os.path.join(models_dir, "phishing_detector_rf.joblib")
    joblib.dump(model_artifact, model_save_path)
    print(f"[8] Serialized model bundle exported to: {model_save_path}")

    # 9. Write evaluation metrics markdown file
    eval_md_path = os.path.join(results_dir, "evaluation_metrics.md")
    with open(eval_md_path, "w", encoding="utf-8") as f:
        f.write("# Model Training & Evaluation Report\n\n")
        f.write(f"- **Task:** Zero-Day Phishing & Malicious URL Classification\n")
        f.write(f"- **Dataset Size:** {len(df)} URLs (Balanced: 50% Benign, 50% Malicious)\n")
        f.write(f"- **Train/Test Split:** 80% / 20% Stratified\n\n")
        f.write("## 1. Comparative Performance\n\n")
        f.write("| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
        f.write(f"| **Logistic Regression (Baseline)** | {acc_base*100:.2f}% | {precision_score(y_test, y_pred_base)*100:.2f}% | {recall_score(y_test, y_pred_base)*100:.2f}% | {f1_base:.4f} | {roc_base:.4f} |\n")
        f.write(f"| **Random Forest Classifier (Ensemble)** | **{acc_rf*100:.2f}%** | **{prec_rf*100:.2f}%** | **{rec_rf*100:.2f}%** | **{f1_rf:.4f}** | **{roc_rf:.4f}** |\n\n")
        f.write("## 2. Confusion Matrix (Random Forest)\n\n")
        f.write(f"- True Negatives (Correctly Identified Benign): **{cm_rf[0,0]}**\n")
        f.write(f"- False Positives (Benign misclassified as Malicious): **{cm_rf[0,1]}**\n")
        f.write(f"- False Negatives (Malicious missed): **{cm_rf[1,0]}**\n")
        f.write(f"- True Positives (Correctly Flagged Attacks): **{cm_rf[1,1]}**\n\n")
        f.write("## 3. Top Feature Importances\n\n")
        for tf in top_features:
            f.write(f"- `{tf['feature']}`: {tf['importance']*100:.2f}%\n")
    print(f"[9] Evaluation markdown report generated at: {eval_md_path}")
    print("\n[+] Training Pipeline Completed Successfully!")

if __name__ == "__main__":
    run_training_pipeline()
