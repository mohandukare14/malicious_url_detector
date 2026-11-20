# ZEAL EDUCATION SOCIETY’S
# ZEAL COLLEGE OF ENGINEERING AND RESEARCH
### NARHE │ PUNE - 41 │ INDIA
### Department Of Artificial Intelligence & Machine Learning (AIML)
**(Accredited with Grade 'A' by NAAC)**

---

| Record No.: ZCOER-ACAD/R/44A | Revision: 00 | Date: 01/04/2021 |
| :--- | :--- | :--- |

## **PROJECT SYNOPSIS**

**Department:** Artificial Intelligence & Machine Learning (AIML)  
**Academic Year:** 2026–2027 &nbsp;&nbsp;&nbsp;&nbsp; **Semester:** II &nbsp;&nbsp;&nbsp;&nbsp; **Div:** C_C1 &nbsp;&nbsp;&nbsp;&nbsp; **Team Name:** THE SCABBARDS &nbsp;&nbsp;&nbsp;&nbsp; **Date:** 21/11/2026  

---

### 1) Name of the College:
**Zeal College of Engineering & Research, Narhe, Pune - 41**

### 2) Name of the Course:
**Bachelor of Engineering (B.E.) in Artificial Intelligence & Machine Learning (AIML)**

### 3) Name of the Students & Group Details:

| Team / Group | Names of the Students | Project / Dissertation Title | Guide / Advisor |
| :---: | :--- | :--- | :--- |
| **THE SCABBARDS**<br>(Div: C_C1) | 1. **Aditya Dhanure** (Roll No: AM1309)<br>2. **Mohan Dukare** (Roll No: AM1311)<br>3. **Vedant Jadhav** (Roll No: AM1315)<br>4. **Prem Jha** (Roll No: AM1317) | **Zero-Day Phishing & Malicious URL Classification Using Machine Learning Analytics** | **Prof. Kajal Gauddab**<br>(Assistant Professor, Dept. of AIML) |

### 4) Date of Project Registration:
**21/11/2026**

### 5) Name of the Guide:
**Prof. Kajal Gauddab** (Assistant Professor, Dept. of AIML)

### 6) Proposed Title:
**Zero-Day Phishing & Malicious URL Classification Using Machine Learning Analytics**

---

### 7) Relevance:
The project falls squarely under the intersection of **Cybersecurity, Machine Learning, and Threat Intelligence**. 

In modern enterprise and personal computing, web browsers and email gateways serve as primary vectors for credential theft, malware distribution, and identity fraud. Conventional defensive mechanisms—predominantly static URL blacklists (such as Google Safe Browsing and DNS sinkholes)—suffer from an inherent temporal vulnerability: they can only block a malicious domain *after* it has already compromised initial victims and been manually reported. 

Machine Learning and predictive analytics revolutionize this paradigm by enabling **zero-day heuristic threat classification**. By extracting deep lexical characteristics, domain entropy, character distributions, and structural syntax directly from raw Uniform Resource Locators (URLs), machine learning algorithms make instantaneous millisecond-level threat determinations without requiring network sandboxing or active page crawling. This proactive detection capability provides foundational security for next-generation Secure Web Gateways (SWG), Email Security Gateways (ESG), and Security Operations Centers (SOC).

---

### 8) Introduction:
In today’s hyper-connected digital landscape, phishing attacks, credential harvesting, and malicious URLs represent over 80% of reported enterprise security breaches and fraud incidents. Cybercriminals leverage automation, Domain Generation Algorithms (DGA), and dynamic bulletproof hosting to spin up thousands of deceptive, short-lived domains within minutes. These malicious URLs mimic reputable banking, e-commerce, cloud storage, and social networking services (e.g., PayPal, Apple ID, Microsoft 365, Chase) using techniques such as typo-squatting, subdomain cloaking, and character obfuscation.

Once a victim is deceived into visiting these landing pages, confidential credentials, financial keys, and session tokens are exfiltrated, or drive-by ransomware is delivered. Because malicious domains now routinely register legitimate SSL/TLS certificates (over 80% of phishing sites use HTTPS), protocol-level trust indicators are no longer sufficient to verify website legitimacy. 

Consequently, there is an urgent industry requirement for an autonomous, lightweight, and high-accuracy Machine Learning system capable of inspecting structural URL indicators in real time. This project establishes an end-to-end predictive cybersecurity pipeline that ingests raw URLs, extracts 19 multi-dimensional lexical and statistical features, and performs high-confidence binary classification (Benign vs. Malicious) before the user establishes connection with the remote host.

---

### 9) Literature Review:

| Sr. No. | Author | ML Algorithms Used | Classifiers | Datasets Used | Optimizers / Criteria | Activation / Splits | Accuracy (%) |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | **Muhammad Zeeshan et al.** | Deep Learning, LSTM | Multiclass | UNSW-NB15, Bot-IoT | Adam | ReLU | **97.10%** |
| 2 | **O. K. Sahingoz et al.** | Random Forest, Decision Tree | Binary & Multiclass | UNB ISCX-URL2016 | Gini / Entropy | Tree Splits | **97.98%** |
| 3 | **A. Al-Ahmadi et al.** | Deep Learning, Bi-LSTM | Binary Classification | Kaggle Phishing Bench | RMSprop | ReLU, Softmax | **98.12%** |
| 4 | **R. S. Rao & A. R. Pais** | Heuristic Rules, SVM | Binary Classification | UCI Repository | SMO / L-BFGS | RBF Kernel | **96.80%** |
| 5 | **Proposed Work (THE SCABBARDS)** | **Random Forest & Logistic Reg.** | **Binary (Safe vs Malicious)** | **PhishTank + Tranco (1500)** | **Gini / L-BFGS** | **120 Ensembles** | **99.67% (99.83% CV)** |

---

### 10) Objectives:
1. **Comprehensive Literature Review:** To conduct an extensive analytical survey of existing statistical and machine learning methodologies for malicious URL and phishing detection.
2. **Multi-Dimensional Feature Engineering:** To construct a robust feature extraction engine capable of deriving 19 lexical, structural, statistical (Shannon entropy), and keyword-based threat vectors from raw URLs.
3. **De-Biased Dataset Ingestion:** To assemble a balanced benchmark dataset of verified benign and malicious domains with protocol parity (accounting for modern HTTPS phishing) to avoid shortcut overfitting.
4. **Machine Learning Model Development & Optimization:** To design, train, and validate baseline (Logistic Regression) and advanced ensemble (Random Forest) classification models with 5-fold Stratified Cross-Validation.
5. **Real-Time Explainable Threat Inference:** To engineer an operational, millisecond-latency prediction module delivering actionable threat classification, confidence scoring, and interpretable indicator flags.

---

### 11) Proposed Work:
The proposed project follows an industry-aligned Machine Learning engineering lifecycle:

1. **Collection of Benchmark Datasets:** Ingesting verified malicious and phishing URLs (from PhishTank, threat intelligence feeds) and legitimate domains (from Tranco, Alexa top sites, academic portals).
2. **Lexical & Entropy Feature Extraction:** Deriving 19 discriminative features including URL length, domain length, character ratios, digit density, IP address in hostname, Shannon entropy, and sensitive keyword presence.
3. **Exploratory Data Analysis (EDA) & Cleaning:** Normalizing bare domains, balancing protocol distributions, and performing stratified 80/20 train-test partitioning.
4. **Model Architecture Selection:** Establishing a standardized Logistic Regression baseline and developing a Random Forest Ensemble (120 estimators, depth-constrained to avoid overfitting).
5. **Model Training & Cross-Validation:** Performing 5-Fold Stratified Cross-Validation to guarantee generalization and evaluate Precision, Recall, F1-Score, and ROC-AUC.
6. **Evaluation, Serialization & Inspection Tool:** Serializing the trained artifact (`.joblib`), outputting performance matrices, and constructing a standalone CLI tool for real-time URL inspection.

---

### 12) Undertaking by the Guide:
The information given by us is correct and the necessary computing and software facilities are available at the institute.

<br><br><br>
_________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _________________________  
**Prof. Kajal Gauddab** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Mini Project Coordinator**  
*(Guide - Dept. of AIML)*

<br><br>
_________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _________________________  
**Academic Coordinator** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Head of the Department (AIML)**  
