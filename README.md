📧 Spam Email Classifier (Local Streamlit App)

This is a simple, local Spam Email Classifier built using Machine Learning, NLP, and a user interface powered by Streamlit. It allows users to input email content and instantly see whether it's Spam 🚫 or Not Spam ✅.

🔍 Features
Easy-to-use interface with Streamlit

Classifies any message/email content

Machine learning model trained using Naive Bayes

Text preprocessing using NLTK (stopwords removal, lowercase, etc.)

Works entirely on your local machine — no internet needed for predictions

🛠️ Tech Stack
Python 3.x

Streamlit

scikit-learn

NLTK

Pandas

Joblib
🚀 How to Run the App Locally
Follow these steps on your computer

1. Clone the Project
bash
git clone https://github.com/your-username/spam-email-classifier.git
cd spam-email-classifier
2. Set up a Virtual Environment (optional but recommended)
bash
python -m venv venv
venv\Scripts\activate     # On Windows
3. Install Required Packages
bash
pip install -r requirements.txt
4. Train the Model
bash
python train_model.py
This will create model.pkl and vectorizer.pkl in your folder.
5. Run the App
bash
streamlit run app.py
✅ Example Use
Input Text:
You've won a free iPhone! Click here to claim now.
Prediction:
🚫 Spam
📁 Project Structure

spam_classifier_app/
├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
├── archive/spam.csv

🌐 Deploying Online (Streamlit Cloud)
Push your complete project to a GitHub repository.
Go to https://streamlit.io/cloud and sign in with your GitHub account.
Click “New App”, choose your repo, and set the main file path as app.py.
Click Deploy. That’s it — your app will be live and sharable! ✅

Make sure these files are committed to GitHub:

app.py

train_model.py

model.pkl

vectorizer.pkl

requirements.txt

README.md

archive/spam.csv

👩‍💻 Author
Bojja Sanjana
A self-driven Python and ML enthusiast ✨

