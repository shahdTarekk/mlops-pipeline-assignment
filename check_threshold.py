import sys

THRESHOLD = 0.85

def main():
    with open("model_info.txt", "r") as f:
        lines = f.read().splitlines()

    run_id = lines[0].strip()
    accuracy = float(lines[1].strip())

    print(f"Run ID: {run_id}")
    print(f"Accuracy: {accuracy:.4f}")

    if accuracy < THRESHOLD:
        print("Failed: accuracy is below 0.85")
        sys.exit(1)

    print("Passed: accuracy is above threshold")

if __name__ == "__main__":
    main()
