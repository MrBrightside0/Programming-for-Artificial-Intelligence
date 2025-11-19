from sklearn.linear_model import LogisticRegression


def train_model(X_train, y_train):
    """
    Trains a multinomial Logistic Regression model.
    """
    model = LogisticRegression(
        multi_class="multinomial",
        solver="lbfgs",
        max_iter=2000
    )
    model.fit(X_train, y_train)
    return model


def predict(model, X_test):
    """
    Generates predictions from the trained model.
    """
    return model.predict(X_test)
