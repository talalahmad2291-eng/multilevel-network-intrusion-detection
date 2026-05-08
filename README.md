# Multilevel Network Intrusion Detection System

This project implements a two-stage AI-based Network Intrusion Detection System (NIDS) using the UNSW-NB15 dataset and machine learning models.

---

# Project Goal

The system works in two stages:

1. classify whether network traffic is:
   - normal
   - attack

2. if the traffic is malicious, classify the:
   - attack category/type

The project uses machine learning techniques to improve intrusion detection accuracy and analyze malicious network behavior.

---

# Dataset

This project uses the UNSW-NB15 dataset for network intrusion detection.

Dataset information and source details are available in:

```text
data/README.md
```

The raw dataset files are not uploaded to GitHub because of large file sizes.

---

# Preprocessing Overview

The dataset preprocessing pipeline includes:

- standardizing column names
- checking missing values and duplicate rows
- separating categorical and numerical features
- one-hot encoding categorical columns:
  - `proto`
  - `service`
  - `state`
- scaling numerical features using `StandardScaler`
- preparing binary labels for intrusion detection
- preparing multi-class labels for attack classification
- encoding attack categories using `LabelEncoder`

---

# Models Used

## Binary Classification Models

- Logistic Regression
- Random Forest Classifier
- Decision Tree Classifier

## Attack Type Classification

- Random Forest Classifier

---

# Results

| Task | Best Model | Accuracy |
|---|---|---|
| Binary Intrusion Detection | Decision Tree | 87.27% |
| Attack Type Classification | Random Forest | 80.26% |

Detailed evaluation results are available in:

```text
results/NIDS_Project_Results.docx
```

---

# Folder Structure

```text
multilevel-network-intrusion-detection/
│
├── data/
│   └── README.md
│
├── docs/
│   └── proposal and project deliverables
│
├── notebooks/
│   └── AI_NIDS.ipynb
│
├── results/
│   └── NIDS_Project_Results.docx
│
├── src/
│   └── app.py
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone <your-repository-link>
cd multilevel-network-intrusion-detection
```

---

## 2. Install Required Libraries

```bash
pip install pandas numpy scikit-learn matplotlib streamlit joblib
```

---

## 3. Run the Jupyter Notebook

Open the notebook:

```text
notebooks/AI_NIDS.ipynb
```

Run all cells to:
- preprocess the dataset
- train the models
- evaluate results
- save trained `.pkl` model files

---

## 4. Run the Streamlit Application

Navigate to the `src` folder and run:

```bash
cd src
streamlit run app.py
```

The application will open in the browser and allow CSV upload for intrusion prediction.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

# Future Improvements

Possible future improvements include:

- real-time traffic monitoring
- deep learning models
- hyperparameter tuning
- handling class imbalance using SMOTE
- deployment using Flask or FastAPI
- live dashboard integration

---

# Repository Contents

The repository includes:

- machine learning notebooks
- preprocessing pipeline
- trained model integration
- Streamlit testing application
- project documentation
- results documentation
