import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

# Load model and vectorizer
model = pickle.load(open("D:/ML PROJECTS/Fake news detection/fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("D:/ML PROJECTS/Fake news detection/tfidf_vectorizer.pkl", "rb"))

# Streamlit UI
st.set_page_config(page_title="📰 Fake News Detector", layout="centered")
st.title("📰 Fake News Detection App")
st.write("Enter or paste a news article to check if it's **Fake** or **Real**.")

# Input text
news_input = st.text_area("📄 Paste News Content Here:")

# Predict button
if st.button("Predict"):
    if news_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        # Transform and predict
        text_vector = vectorizer.transform([news_input])
        prediction = model.predict(text_vector)[0]
        probability = model.predict_proba(text_vector)[0]

        label = "🟥 FAKE NEWS" if prediction == 1 else "🟩 REAL NEWS"
        confidence = round(np.max(probability) * 100, 2)

        st.subheader(label)
        st.write(f"🔍 **Confidence:** {confidence}%")
