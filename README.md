
# 📧 Spam Email Classifier using Streamlit and Machine Learning

This is a simple and interactive spam detection system built using **Python**, **Machine Learning**, and **Streamlit**. The app classifies email or message content as **Spam** or **Not Spam** based on the text input provided by the user.

---

## 🔍 Features

- 🔹 User-friendly interface built with Streamlit  
- 🔹 Paste any email/message text to check for spam  
- 🔹 Instant predictions: 🚫 Spam or ✅ Not Spam  
- 🔹 Built using Naive Bayes classifier  
- 🔹 Text preprocessing with NLTK stopwords  
- 🔹 Lightweight, fast, and easy to use  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- NLTK  
- Pandas  
- Joblib  

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/spam-email-classifier.git
cd spam-email-classifier

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Train the model (only once)
python train_model.py

# Run the Streamlit app
streamlit run app.py
```

---

## ✅ Example

**Input Text:**  
```
Congratulations! You have won a free vacation. Click the link to claim your prize!
```

**Prediction:**  
```
🚫 Spam
```

Try other examples like:  
- `Win cash now! Limited time offer!` → 🚫 Spam  
- `Hey, just checking in. Are we still meeting tomorrow?` → ✅ Not Spam  

---

## 📁 Project Structure

```
spam_classifier_app/
├── app.py                # Streamlit UI
├── train_model.py        # Model training script
├── model.pkl             # Saved trained model
├── vectorizer.pkl        # Saved CountVectorizer
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── archive/
    └── spam.csv          # Dataset from Kaggle
```

---

## 🌐 Deploying Online (Streamlit Cloud)

You can easily deploy this app online using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push your project to GitHub.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in with GitHub.
3. Click **New App**.
4. Select your GitHub repo and choose `app.py` as the entry point.
5. Click **Deploy** — your app will be live in seconds!

**Ensure these files are in your GitHub repo:**
- `app.py`
- `train_model.py`
- `model.pkl`
- `vectorizer.pkl`
- `requirements.txt`
- `archive/spam.csv`
- `README.md`

---

## 👩‍💻 Author

**Bojja Sanjana**  
A self-driven Python and Machine Learning enthusiast ✨  

---
