# Fake-News-Detector

A machine learning project that classifies news articles as **Fake** or **Real** using TF-IDF vectorization and Logistic Regression. The model is deployed as a Streamlit web application with an interactive UI for real-time predictions.

---

## 📌 Project Features

- ✅ TF-IDF based NLP pipeline
- ✅ Logistic Regression classifier
- ✅ Evaluation using Accuracy, Precision, Recall, F1-score
- ✅ Confusion matrix & top indicator words
- ✅ Interactive UI using Streamlit
- ✅ Can be deployed locally or online

---

## 📂 Dataset

- Source: [Fake and Real News Dataset – Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- Files used:
  - `Fake.csv` (label = 1)
  - `True.csv` (label = 0)
- Total articles: `~45,000`

---

## 🧠 Model Overview

| Technique | Details |
|----------|---------|
| Vectorizer | TF-IDF (`max_df=0.7`, `stop_words=english`) |
| Classifier | Logistic Regression |
| Train/Test Split | 80/20 |
| Labels | `0 = Real`, `1 = Fake` |

---

## 📊 Evaluation Metrics

Accuracy : 0.9842
Precision : 0.9855
Recall : 0.9826
F1-Score : 0.9840

markdown
Copy
Edit

📋 **Classification Report**:
Real News: Precision = 0.98 | Recall = 0.99 | F1 = 0.98
Fake News: Precision = 0.99 | Recall = 0.98 | F1 = 0.98

yaml
Copy
Edit

---

## 📈 Visualizations

### 🔷 Confusion Matrix

![image](https://github.com/user-attachments/assets/ba6c9ef9-3701-4a59-bcee-7c8c803f0d5e)


### 🔴 Top Fake News Indicators (Words)

![image](https://github.com/user-attachments/assets/4f2de3ba-c53f-4175-a125-5c7d5d254f31)

### 🟢 Top Real News Indicators (Words)

![image](https://github.com/user-attachments/assets/a2df1fef-9f1a-4094-a53a-1748b11487bb)


---

## 💻 Streamlit Frontend

### 🎯 Features:
- Text box to paste news
- Predict button
- Displays label + confidence
- Lightweight and fast UI

### 🧪 Sample UI Screenshot:

![image](https://github.com/user-attachments/assets/8f926c39-2e8d-4a55-9d2d-17e164512a69)


---

## 🚀 How to Run Locally

### 🛠 Prerequisites:
- Python 3.8+
- Streamlit
- scikit-learn
- Pandas, NumPy

### 🔧 Install requirements (optional)
```bash
pip install streamlit scikit-learn pandas numpy
▶️ Run the App
bash
Copy
Edit
streamlit run fake_news_app.py
App will open at http://localhost:8501

📁 Project Structure
graphql
Copy
Edit
📦 Fake News Detection
├── Fake.csv
├── True.csv
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
├── fake_news_confusion_matrix.png
├── top_fake_words.png
├── top_real_words.png
├── fake_news_app.py
├── README.md
📌 To-Do
 Add title-based prediction fallback

 Deploy to Streamlit Cloud

 Add support for news URL fetching

 Add language detection + multilingual support

👨‍💻 Developed By
V. Yuvan Krishnan
Student, SRM Institute of Science & Technology
