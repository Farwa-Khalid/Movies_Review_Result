# 🎬 Sentiment Analysis Web App  

I built a simple **Sentiment Analysis Web Application** to understand the end-to-end workflow of an NLP project — from raw data to a deployed web app.

---

## 🚀 Project Overview

This project performs **binary sentiment classification** on movie reviews (**Positive / Negative**) using:

- TF-IDF Vectorization  
- Logistic Regression  
- Flask Web Framework  

The application allows users to enter a movie review and instantly receive a sentiment prediction.

---

## 📌 What I Did in This Project

- Loaded and explored a dataset of movie reviews using **pandas**
- Cleaned text data:
  - Converted text to lowercase  
  - Removed punctuation  
  - Removed extra spaces  
- Converted text into numerical features using **TF-IDF**
- Trained a **Logistic Regression** model
- Achieved approximately **~89% accuracy**
- Saved the trained model using **joblib**
- Built a simple web interface using **Flask**
- Integrated the ML model into the web app for real-time predictions

---

## 🧠 Key Learnings

This project helped me understand:

- How NLP data differs from structured numeric datasets  
- The importance of text preprocessing  
- Feature extraction using TF-IDF  
- Model training and evaluation workflow  
- How to integrate ML models into web applications  
- The complete end-to-end pipeline from raw data to working app  

> The best way to learn Machine Learning is by building real projects.

---

## 🛠️ Tech Stack

- Python  
- pandas  
- scikit-learn  
- TF-IDF Vectorizer  
- Logistic Regression  
- joblib  
- Flask  

---

## 💻 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Farwa-Khalid/Movies_Review_Result.git
```

### 2️⃣ Navigate into the project
```bash
cd Movies_Review_Result
```

### 3️⃣ Install dependencies (if requirements.txt exists)
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app
```bash
python application.py
```

### 5️⃣ Open in your browser
```
http://127.0.0.1:5000
```


