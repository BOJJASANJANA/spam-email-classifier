# app.py
import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download stopwords (only once)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

# Load model/vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def preprocess(text):
    text = text.lower()
    text = "".join([ch for ch in text if ch not in string.punctuation])
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stop_words]
    return " ".join(words)

# Streamlit app UI
st.set_page_config(page_title="Spam Classifier", page_icon="📧")
st.title("📧 Spam Email Classifier")
st.write("Enter an email message below and classify it as spam or not.")

input_text = st.text_area("✍️ Enter your message:")

if st.button("🔍 Classify"):
    if not input_text.strip():
        st.warning("⚠️ Please enter a message before classifying.")
    else:
        processed = preprocess(input_text)
        vect_text = vectorizer.transform([processed])
        prediction = model.predict(vect_text)[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Prediction: {label}")
