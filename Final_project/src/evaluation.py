import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def evaluate_model(y_test, y_pred, save_path="results/"):
    """
    Computes performance metrics and saves them into text files.
    """

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="weighted")
    rec = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")

    metrics_text = (
        f"Accuracy: {acc}\n"
        f"Precision: {prec}\n"
        f"Recall: {rec}\n"
        f"F1 Score: {f1}\n"
    )

    with open(save_path + "metrics.txt", "w") as f:
        f.write(metrics_text)

    with open(save_path + "classification_report.txt", "w") as f:
        f.write(classification_report(y_test, y_pred))

    return acc, prec, rec, f1


def plot_confusion_matrix(y_test, y_pred, save_path="figures/"):
    """
    Saves a confusion matrix figure.
    """
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt="g")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig(save_path + "confusion_matrix.png", dpi=300)
    plt.close()
