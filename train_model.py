import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import nltk
from nltk.corpus import stopwords
import joblib

nltk.download('stopwords')

# Sample spam dataset
data = {
    "text": [
        "Congratulations! You have won a free iPhone. Click here to claim.",
        "Reminder: Your bill is due tomorrow. Please pay on time.",
        "You are selected for a ₹1,00,000 prize. Click to win now.",
        "Hey, just checking in about tomorrow’s meeting.",
        "Win a brand new bike by entering this lucky draw.",
        "Your Amazon order has been shipped.",
        "Urgent! Your account has been compromised. Verify now!",
        "Lunch at 1pm today?",
        "You’ve been chosen for an exclusive credit card offer!",
        "Can you send me the project report by EOD?"
    ],
    "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

# Preprocess
stop_words = set(stopwords.words("english"))
df["text_clean"] = df["text"].apply(lambda x: " ".join([word for word in x.lower().split() if word not in stop_words]))

# Features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text_clean"])
y = df["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("✅ Model and vectorizer saved!")
