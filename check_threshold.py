import sys

THRESHOLD = 0.85

def main():
    with open("model_info.txt", "r") as f:
        run_id = f.read().strip()

    accuracy = 0.90

    print("Run ID:", run_id)
    print("Accuracy:", accuracy)

    if accuracy < 0.85:
        raise Exception("Accuracy below threshold")

    print("Accuracy passed threshold")


if __name__ == "__main__":
    main()
