
# 🧠 Supervised Learning: Cancer Diagnostic System

A machine learning implementation for **Breast Cancer Classification** using Python and Scikit-learn.

## 🚀 Description

This project implements a supervised learning pipeline to classify tumors as **Malignant** or **Benign** based on the Wisconsin Diagnostic Dataset. The system performs the following steps:

1.  **Data Loading:** Extraction of 30 cellular features.
2.  **Preprocessing:** Cleaning and normalization using `StandardScaler`.
3.  **Modeling:** Implementation of **Logistic Regression**.
4.  **Evaluation:** Metric analysis (Accuracy, Recall, ROC-AUC).

It serves as the "Actividad Fundamental 6" for the Machine Learning course.

## 🧩 Project Structure

AF6_Supervised_Model/
├── cancer_model.py      # Main script for training and evaluation
├── README.md            # Project documentation
└── requirements.txt     # Dependencies (optional)

## ⚙️ Installation

Navigate to the project folder:
cd AF6_Supervised_Model

Install dependencies:
pip install pandas numpy scikit-learn matplotlib seaborn

## ▶️ Usage

To train the model and visualize results, run:
python cancer_model.py

The script will output the classification report in the terminal and display the **Confusion Matrix** plot automatically.

## 📊 Key Metrics

| Metric | Value (Approx) | Description |
| :--- | :--- | :--- |
| **Accuracy** | 98% | Overall correct predictions |
| **Recall (Malignant)** | 94% | Ability to detect actual cancer cases |
| **ROC-AUC** | 0.99 | Separation capability between classes |

## 👨‍💻 Authors

Edmundo Ramses Moreno González
Bachelor in Artificial Intelligence Engineering
Universidad Autónoma de Nuevo León – FIME

## 🔗 Repository

https://github.com/[TU-USUARIO]/[TU-REPO]