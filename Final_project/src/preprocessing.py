import pandas as pd
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_dataset():
    """
    Loads the digits dataset from sklearn and returns a pandas DataFrame.
    """
    digits = load_digits()
    X = pd.DataFrame(digits.data)
    y = pd.Series(digits.target, name="target")

    df = pd.concat([X, y], axis=1)
    return df


def split_features(df):
    """
    Splits the DataFrame into features and target.
    """
    X = df.drop("target", axis=1)
    y = df["target"]
    return X, y


def scale_features(X_train, X_test):
    """
    Applies standard scaling to training and testing data.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled
