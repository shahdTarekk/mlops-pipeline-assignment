import os
import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

FORCE_ACCURACY = os.getenv("FORCE_ACCURACY")

def main():
    X, y = load_iris(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    mlflow.set_experiment("github-actions-validation")

    with mlflow.start_run() as run:
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        accuracy = accuracy_score(y_test, preds)

        if FORCE_ACCURACY is not None and FORCE_ACCURACY != "":
            accuracy = float(FORCE_ACCURACY)

        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_metric("accuracy", accuracy)

        run_id = run.info.run_id

        with open("model_info.txt", "w") as f:
            f.write(f"{run_id}\n")
            f.write(f"{accuracy}\n")

        print(f"Run ID: {run_id}")
        print(f"Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    main()
