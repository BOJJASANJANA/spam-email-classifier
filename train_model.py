import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import nltk
from nltk.corpus import stopwords
import joblib
import string

# Download stopwords if not already
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))

# 🔹 Load dataset from archive folder
df = pd.read_csv("archive/spam.csv", encoding='latin-1')

# 🔹 Keep only relevant columns and rename
df = df[["v1", "v2"]]
df.columns = ["label", "text"]

# 🔹 Convert labels to binary (ham = 0, spam = 1)
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# 🔹 Clean text: lowercase, remove punctuation, stopwords
def preprocess(text):
    text = text.lower()
    text = "".join([ch for ch in text if ch not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df["text_clean"] = df["text"].apply(preprocess)

# 🔹 Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text_clean"])
y = df["label"]

# 🔹 Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# 🔹 Evaluate model
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# 🔹 Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("✅ Model and vectorizer saved successfully!")
