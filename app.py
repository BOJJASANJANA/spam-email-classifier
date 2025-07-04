# app.py
import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

# Load model/vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
ps = PorterStemmer()

def preprocess(text):
    text = text.lower()
    text = "".join([ch for ch in text if ch not in string.punctuation])
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stopwords.words('english')]
    return " ".join(words)

# Streamlit app UI
st.set_page_config(page_title="Spam Classifier", page_icon="📧")
st.title("📧 Spam Email Classifier")
st.write("Enter an email message below and classify it as spam or not.")

input_text = st.text_area("Enter your message:")

if st.button("Classify"):
    processed = preprocess(input_text)
    vect_text = vectorizer.transform([processed])
    prediction = model.predict(vect_text)[0]
    label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
    st.subheader(f"Prediction: {label}")
