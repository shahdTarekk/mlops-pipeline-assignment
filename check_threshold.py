import mlflow
import sys

THRESHOLD = 0.85

def main():
    with open("model_info.txt", "r") as f:
        run_id = f.read().strip()

    client = mlflow.tracking.MlflowClient()
    run = client.get_run(run_id)

    accuracy = run.data.metrics.get("accuracy")

    if accuracy is None:
        print("Error: accuracy metric not found.")
        sys.exit(1)

    print(f"Run ID: {run_id}")
    print(f"Accuracy: {accuracy:.4f}")

    if accuracy < THRESHOLD:
        print("Failed: accuracy is below 0.85")
        sys.exit(1)

    print("Passed: accuracy is above threshold")

if __name__ == "__main__":
    main()
