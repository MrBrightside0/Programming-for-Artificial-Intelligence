import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

# Load dataset directly from sklearn
data = load_breast_cancer()

# Create DataFrame for analysis
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target  # 0: Malignant, 1: Benign

print(">>> Dataset Loaded")
print(f"Shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}") 

# Split features and target
X = df.drop('target', axis=1)
y = df['target']

# Split into training (70%) and testing (30%)
# Using a fixed random state for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalize data using StandardScaler
# This is crucial for Logistic Regression to avoid bias from large-scale features like 'Area'
scaler = StandardScaler()

# Fit only on training data to prevent data leakage
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Comparison for the technical report (Raw vs Scaled)
print("\n>>> Normalization Check (Feature: mean area)")
print(f"Raw value:    {X_train.iloc[0]['mean area']:.2f}")
print(f"Scaled value: {X_train_scaled[0][3]:.4f}")

# Initialize and train the Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)
print("\n>>> Model trained successfully")

# Evaluation metrics
y_pred = model.predict(X_test_scaled)

print("\n>>> Classification Report")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# ROC-AUC Score
auc = roc_auc_score(y_test, y_pred)
print(f"ROC-AUC Score: {auc:.4f}")

# Visualizing results with a Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=data.target_names,
            yticklabels=data.target_names)
plt.title('Confusion Matrix - Breast Cancer Diagnosis')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.tight_layout()
plt.show()