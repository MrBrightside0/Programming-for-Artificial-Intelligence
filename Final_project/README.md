# 🧠 Multiclass Logistic Regression on the UCI Digits Dataset

A complete **Python-based supervised learning pipeline** built using `pandas`, `scikit-learn`, `numpy`, and `matplotlib`.

This project trains and evaluates a **multiclass logistic regression model** using the real **UCI Optical Recognition of Handwritten Digits** dataset, applying a full workflow of data preprocessing, normalization, model training, and performance evaluation.

## 🚀 Description

The goal of this project is to classify **handwritten digits from 0 to 9** using 64 pixel-intensity features extracted from 8x8 grayscale images.

The system follows the complete supervised learning process:

- Dataset loading and exploration  
- Handling purely numerical features  
- Feature scaling using standardization  
- Train/test split (70% / 30%)  
- Model training using **Logistic Regression (multinomial)**  
- Model evaluation with metrics:  
  - Accuracy  
  - Precision  
  - Recall  
  - F1-score  
- Confusion matrix visualization  
- Optional coefficient analysis to interpret feature importance

Everything is modular, readable, and aligned with the course requirements.

## 🧩 Project Structure

```text
FINAL_PROJECT/
├── data/
│   └── digits.csv
│
├── notebooks/
│   └── Digits_LogReg_Multiclass.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── modeling.py
│   └── evaluation.py
│
├── figures/
│   ├── confusion_matrix.png
│   ├── class_distribution.png
│   └── sample_digits.png
│
├── results/
│   ├── metrics.txt
│   ├── classification_report.txt
│   └── confusion_matrix.csv
│
└── README.md
```

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-user/AF3-PIA-LogReg
```

2. **Navigate to the project folder:**

```bash
cd AF3-PIA-LogisticRegression
```

3. **Create and activate a virtual environment:**

```bash
python -m venv venv
venv/Scripts/activate     # Windows
# or
source venv/bin/activate  # macOS / Linux
```

4. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Open the main notebook:

```bash
jupyter notebook notebooks/Digits_LogReg_Multiclass.ipynb
```

Run all the cells to:

- Load the dataset  
- Scale the input features  
- Train the multinomial logistic regression model  
- Evaluate predictions on the test set  
- Generate all plots inside the `/figures` folder  
- Save metrics and reports inside the `/results` folder  

The notebook is fully self-contained and ready to execute.

## 📊 Output Files

| File | Description |
|------|-------------|
| **confusion_matrix.png** | Confusion matrix for model evaluation |
| **class_distribution.png** | Visualization of target class distribution |
| **sample_digits.png** | Grid of sample handwritten digits from the dataset |
| **metrics.txt** | Accuracy, precision, recall, and F1-score summary |
| **classification_report.txt** | Full sklearn classification report |
| **confusion_matrix.csv** | Confusion matrix saved as a CSV table |

All figures are automatically saved inside `/figures`, and all metric summaries are saved inside `/results`.

## 🔬 Technologies Used

- Python 3.x  
- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn  
- jupyter notebook  

## 👨‍💻 Authors

**Edmundo Ramses Moreno González**  
Bachelor in Artificial Intelligence Engineering  
Universidad Autónoma de Nuevo León – FIME

**Antonio Andre Martinez Martinez**  
Bachelor in Artificial Intelligence Engineering  
Universidad Autónoma de Nuevo León – FIME

## 🔗 Dataset Source

UCI Machine Learning Repository – Optical Recognition of Handwritten Digits  
https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits

## 📚 Notes

The project strictly follows the requirements for:

- Supervised learning methodology  
- Multiclass logistic regression (`LogisticRegression(multi_class='multinomial')`)  
- Data preprocessing and feature scaling  
- Evaluation metrics and critical analysis  
- Clean, documented and reproducible code

Everything is fully organized for academic submission and GitHub best practices.
