# Simple AI model project

def predict(value):
    if value >= 50:
        return "Positive"
    return "Negative"


if __name__ == "__main__":
    result = predict(75)
    print("Prediction:", result)
