from flask import Flask,request,jsonify,render_template # type: ignore
import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

application = Flask(__name__)
app=application

sentiment_model=joblib.load('models/sentiment_model.pkl')
tfidf_vectorizer=joblib.load('models/tfidf_vectorizer.pkl')

@app.route("/")
def index():
      return render_template('home.html')
  

@app.route("/prediction", methods=["POST"])
def prediction():
    # get review from form
    review = request.form['review']

    # clean the text same as training
    import re
    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    clean_review = clean_text(review)

    # transform using loaded TF-IDF vectorizer
    review_vector = tfidf_vectorizer.transform([clean_review])

    # predict using loaded model
    pred = sentiment_model.predict(review_vector)[0]

    sentiment = "Positive 😊" if pred == 1 else "Negative 😞"

    return render_template('home.html', prediction_text=f"Sentiment: {sentiment}")


if __name__=="__main__":
    application.run(host="0.0.0.0")

