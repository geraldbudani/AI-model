import joblib

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_text(text: str) -> str:
    """
Predicts if a given text is Spam or Ham.
    """
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return "Spam" if prediction == 1 else "Ham"

if __name__ == "__main__":
    # Example predictions
    samples = [
        "Congratulations! You won a free iPhone. Click here to claim.",
        "Hey Gerald, are we meeting tomorrow at 10?",
        "Free entry in 2 a weekly competition to win tickets!",
        "I'll call you when I'm done with class."
    ]

    for s in samples:
        print(f"Text: {s}\nPrediction: {predict_text(s)}\n")
