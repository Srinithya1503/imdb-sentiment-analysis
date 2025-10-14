# 🤖 Trained Models Directory

This folder contains serialized machine learning models and feature vectorizers used for sentiment classification.

## 📁 Contents

### Model Files

| File | Model Type | Description |
|------|-----------|-------------|
| `logistic_regression.pkl` | Logistic Regression | Best performing model; fast and interpretable |
| `naive_bayes.pkl` | Multinomial Naïve Bayes | Fast inference; probabilistic approach |
| `svm_model.pkl` | Linear SVM | Support Vector Machine; robust classifier |
| `tfidf_vectorizer.pkl` | TF-IDF Vectorizer | Feature transformation; MUST load first |

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Logistic Regression** | **0.8920** | 0.8950 | 0.8890 | 0.8920 |
| Naïve Bayes | 0.8650 | 0.8720 | 0.8570 | 0.8640 |
| SVM | 0.8850 | 0.8870 | 0.8830 | 0.8850 |

*Metrics computed on 20% test set (10,000 reviews)*

**Recommendation:** Use **Logistic Regression** for best accuracy and interpretability.

## 🚀 How to Use Models

### Option 1: Using Convenience Functions

```python
from src.modeling import predict_sentiment, load_model, load_vectorizer

# Load model and vectorizer
model = load_model('Logistic Regression')
vectorizer = load_vectorizer()

# Make prediction
review = "This movie was absolutely amazing!"
prediction, confidence = predict_sentiment(review, model, vectorizer)

print(f"Sentiment: {prediction}")
print(f"Confidence: {confidence*100:.2f}%")
```

### Option 2: Direct Pickle Loading

```python
import pickle
from src.preprocessing import preprocess_text

# Load vectorizer first (IMPORTANT!)
vectorizer = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))

# Load model
model = pickle.load(open('models/logistic_regression.pkl', 'rb'))

# Preprocess review
review = "This movie was terrible!"
cleaned = preprocess_text(review)

# Vectorize
X = vectorizer.transform([cleaned])

# Predict
prediction = model.predict(X)[0]
confidence = model.predict_proba(X).max()

print(f"Prediction: {prediction} ({confidence*100:.2f}%)")
```

### Option 3: Batch Predictions

```python
from src.utils import batch_predict

reviews = [
    "Amazing film!",
    "Terrible movie",
    "Not bad"
]

results = batch_predict(reviews, model, vectorizer)
print(results)
#    review prediction confidence
# 0  Amazing film!   positive      0.95
# 1  Terrible movie  negative      0.92
# 2  Not bad         positive      0.58
```

## ⚠️ Important Notes

### 1. Load Vectorizer First

**ALWAYS load and use the vectorizer that was used during training:**

```python
# ✓ CORRECT
vectorizer = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
X = vectorizer.transform([cleaned_text])

# ❌ WRONG (will cause errors)
X = some_other_vectorizer.transform([cleaned_text])
```

### 2. Preprocess Text Consistently

Use the same preprocessing pipeline:

```python
from src.preprocessing import preprocess_text

# This is what was used during training
cleaned = preprocess_text(raw_review)
```

### 3. Pickle Security

Only load pickle files from trusted sources. Pickle can execute arbitrary code:

```python
# ✓ SAFE (your own models)
model = pickle.load(open('models/logistic_regression.pkl', 'rb'))

# ❌ UNSAFE (unknown source)
model = pickle.load(open('unknown_model.pkl', 'rb'))
```

### 4. Version Compatibility

Ensure scikit-learn version matches:

```bash
# Check version
python -c "import sklearn; print(sklearn.__version__)"

# Should be 1.3.0 or compatible
pip install scikit-learn==1.3.0
```

## 🔧 Model Details

### Logistic Regression

- **Pros:**
  - Highest accuracy (89.2%)
  - Fast training and inference
  - Interpretable coefficients
  - Works well with TF-IDF features

- **Cons:**
  - Linear decision boundary
  - Less flexible than ensemble methods

- **Parameters:**
  - max_iter: 1000
  - random_state: 42
  - solver: lbfgs (default)

### Naive Bayes

- **Pros:**
  - Very fast inference
  - Lightweight (small model size)
  - Good baseline

- **Cons:**
  - Lower accuracy (86.5%)
  - Assumes feature independence
  - Less robust

- **Type:** Multinomial Naïve Bayes

### Support Vector Machine (SVM)

- **Pros:**
  - Robust classifier (88.5% accuracy)
  - Handles high-dimensional data well
  - Good generalization

- **Cons:**
  - Slower training than Logistic Regression
  - Less interpretable

- **Type:** LinearSVC (linear kernel)

## 💾 Model Serialization

### Saving Models

```python
import pickle
from sklearn.linear_model import LogisticRegression

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save
with open('models/my_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

### Loading Models

```python
with open('models/my_model.pkl', 'rb') as f:
    model = pickle.load(f)
```

### Model File Sizes

| Model | Size |
|-------|------|
| logistic_regression.pkl | ~2.5 MB |
| naive_bayes.pkl | ~1.8 MB |
| svm_model.pkl | ~3.2 MB |
| tfidf_vectorizer.pkl | ~15 MB |

## 🚀 Production Deployment

### Option 1: Flask REST API

```python
from flask import Flask, request, jsonify
import pickle
from src.preprocessing import preprocess_text

app = Flask(__name__)

# Load models on startup
vectorizer = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
model = pickle.load(open('models/logistic_regression.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review = data['review']
    
    # Preprocess and predict
    cleaned = preprocess_text(review)
    X = vectorizer.transform([cleaned])
    prediction = model.predict(X)[0]
    confidence = model.predict_proba(X).max()
    
    return jsonify({
        'sentiment': prediction,
        'confidence': float(confidence)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Run:** `python app_flask.py`

### Option 2: Streamlit Dashboard

```bash
streamlit run app.py
```

### Option 3: Docker Deployment

```dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app_flask.py"]
```

**Build & Run:**
```bash
docker build -t sentiment-model .
docker run -p 5000:5000 sentiment-model
```

## 🔄 Model Retraining

To retrain models with new data:

```bash
python sentiment_analysis.py
```

This will:
1. Load data
2. Preprocess
3. Train all models
4. Save to `models/` folder
5. Overwrite existing models

## 📈 Performance Comparison

```
Accuracy Comparison:
┌─────────────────────┬───────────┐
│ Logistic Regression │ 89.20% ██████████ │
│ SVM                 │ 88.50% █████████░ │
│ Naive Bayes         │ 86.50% ████████░░ │
└─────────────────────┴───────────┘
```

## ❓ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'sklearn'"

```bash
pip install scikit-learn==1.3.0
```

### Error: "FileNotFoundError: tfidf_vectorizer.pkl"

Run the training pipeline:
```bash
python sentiment_analysis.py
```

### Error: "Incompatible version"

Check scikit-learn version:
```bash
python -c "import sklearn; print(sklearn.__version__)"
```

Reinstall if needed:
```bash
pip install --upgrade scikit-learn==1.3.0
```

### Predictions seem random

Make sure you're using the correct vectorizer: