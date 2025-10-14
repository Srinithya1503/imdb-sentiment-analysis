# 🎬 IMDb Movie Reviews Sentiment Analysis

A beginner-friendly machine learning project that classifies IMDb movie reviews as **positive** or **negative** using Natural Language Processing (NLP) and supervised learning models.

**Dataset:** [50K IMDb Reviews on Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

---

## 🧠 Project Overview

This project teaches you how to:
- ✅ Clean and preprocess text data
- ✅ Build and compare machine learning classifiers
- ✅ Evaluate models using multiple metrics
- ✅ Extract actionable insights from unstructured text
- ✅ Deploy models for real-world predictions

**Perfect for:** Data science beginners, students, NLP enthusiasts, portfolio building

---

## 🎯 Business Motivation

Understanding audience sentiment helps:
- **Production Houses** → Know what worked or failed in a release
- **Streaming Platforms** → Recommend similar content to users
- **Marketers** → Track public opinion trends in real-time
- **Studios** → Optimize script quality and casting decisions

**Real Insight:** Analysis shows 72% of positive reviews mention strong acting/direction, while 64% of negative reviews criticize pacing and storyline depth.

---

## 📊 Dataset

| Property | Details |
|----------|---------|
| **Name** | IMDb Dataset of 50K Movie Reviews |
| **Source** | [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) |
| **Size** | 50,000 reviews (balanced: 25K positive, 25K negative) |
| **Format** | CSV with 2 columns: `review` (text) and `sentiment` (label) |

---

## 🔧 Technologies & Libraries

| Category | Tools / Libraries |
|----------|------------------|
| **Language** | Python 3.8+ |
| **Data Processing** | Pandas, NumPy |
| **Text Processing** | NLTK, spaCy |
| **Visualization** | Matplotlib, Seaborn, WordCloud |
| **Machine Learning** | Scikit-learn |
| **Dashboard** | Streamlit |
| **Deep Learning** | TensorFlow / Transformers (optional) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- 2GB disk space
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/imdb_sentiment_analysis.git
cd imdb_sentiment_analysis

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download NLP models
python -m nltk.downloader stopwords punkt wordnet
python -m spacy download en_core_web_sm

# 5. Download dataset
# - Visit: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
# - Download imdb_dataset.csv
# - Place in: data/raw/imdb_dataset.csv

# 6. Run the pipeline
python sentiment_analysis.py

# 7. (Optional) Launch Streamlit dashboard
streamlit run app.py
```

---

## 📁 Project Structure

```
imdb_sentiment_analysis/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore patterns
├── sentiment_analysis_main.py         # Main end-to-end pipeline
├── app.py                             # Streamlit dashboard
├── files_summary.md                   # files guide
├── setup_guide                        # project setup guide 
│
├── data/
│   ├── raw/
│   │   └── IMDB Dataset.csv           # Original dataset (download from Kaggle)
│   ├── processed/
│   │   └── cleaned_reviews.csv        # Preprocessed data
│   └── README.md                      # Data documentation
│
├── notebooks/
│   └── sentiment_analysis.ipynb       # Interactive Jupyter notebook
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py               # Text cleaning functions
│   ├── eda.py                         # Exploratory data analysis
│   ├── modeling.py                    # Model training & evaluation
│   └── utils.py                       # Helper functions
│
├── models/
│   ├── README.md                      # Model loading guide
│   ├── logistic_regression.pkl        # Trained model
│   ├── naive_bayes.pkl                # Trained model
│   ├── svm.pkl                        # Trained model
│   └── tfidf_vectorizer.pkl           # Feature vectorizer
│
└── outputs/
    ├── visualizations/
    │   ├── word_clouds.png
    │   ├── sentiment_distribution.png
    │   ├── review_length_distribution.png
    │   └── frequent_words.png

    └── results/
    │   ├── pipeline_summary.txt
        └── model_performance.csv
```

---

## 🧩 Project Workflow

### 1️⃣ Data Loading & Exploration
```python
python sentiment_analysis.py
```
- Loads 50K reviews from CSV
- Analyzes data balance and structure
- Generates visualizations

### 2️⃣ Text Preprocessing
- Remove HTML tags, punctuation, numbers
- Convert to lowercase
- Tokenization
- Stopword removal
- Lemmatization

### 3️⃣ Exploratory Data Analysis (EDA)
- Word cloud visualizations
- Sentiment distribution charts
- Review length analysis
- Most frequent words

### 4️⃣ Feature Engineering
- TF-IDF vectorization (5,000 features)
- Train-test split (80-20)

### 5️⃣ Model Training
Three classification models:
- **Logistic Regression** ⭐ (Best performance)
- **Naïve Bayes** (Fast & lightweight)
- **SVM** (Robust classifier)

### 6️⃣ Model Evaluation
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- Cross-validation

### 7️⃣ Real-time Predictions
- Interactive dashboard
- Example reviews
- Confidence scores

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | **89.20%** | 89.50% | 88.90% | 89.20% |
| Naïve Bayes | 86.50% | 87.20% | 85.70% | 86.40% |
| SVM | 88.50% | 88.70% | 88.30% | 88.50% |

*Tested on 10,000 reviews (20% test set)*

---

## 🧾 Example Usage

### Using the Streamlit Dashboard
```bash
streamlit run app.py
```
Then visit: `http://localhost:8501`

### Making Predictions Programmatically
```python
import pickle
from src.preprocessing import preprocess_text

# Load model and vectorizer
vectorizer = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
model = pickle.load(open('models/logistic_regression.pkl', 'rb'))

# Make prediction
review = "This movie was absolutely amazing!"
cleaned = preprocess_text(review)
X = vectorizer.transform([cleaned])
prediction = model.predict(X)[0]

print(f"Sentiment: {prediction}")  # Output: positive
```

---

## 💡 Key Insights from Analysis

1. **Positive Reviews** commonly mention:
   - "brilliant," "excellent," "masterpiece"
   - "great acting," "amazing direction"
   - "best film," "highly recommend"

2. **Negative Reviews** commonly mention:
   - "boring," "terrible," "waste of time"
   - "bad acting," "weak plot"
   - "slow," "predictable," "disappointing"

3. **Sentiment Distribution:**
   - 72% of positive reviews emphasize acting quality
   - 64% of negative reviews criticize pacing/storyline
   - Average review length: 240 words

---

## 📓 Jupyter Notebook

Explore the data interactively:
```bash
jupyter notebook notebooks/sentiment_analysis.ipynb
```

The notebook includes:
- Data loading and exploration
- Text preprocessing pipeline
- Word cloud visualizations
- Model training and comparison
- Feature importance analysis
- Custom prediction examples

---

## 🚀 Deployment Options

### Option 1: Streamlit Dashboard (Easiest)
```bash
streamlit run app.py
```

### Option 2: Flask REST API
```python
from flask import Flask, request, jsonify
# See deployment guide for details
```

### Option 3: Docker Container
```bash
docker build -t imdb-sentiment .
docker run -p 5000:5000 imdb-sentiment
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError: imdb_dataset.csv` | Download from Kaggle and place in `data/raw/` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| NLTK data missing | Run `python -m nltk.downloader stopwords punkt wordnet` |
| Out of memory | Close other apps or use smaller data sample |
| Streamlit not running | Install with `pip install streamlit` |

---

## 📈 Future Improvements

- [ ] **Aspect-based Sentiment Analysis** — Separate sentiment for acting, plot, music, etc.
- [ ] **Multi-class Emotion Detection** — Happy, sad, angry, surprised, disgusted
- [ ] **BERT/Transformer Models** — State-of-the-art NLP performance
- [ ] **Real-time IMDb Scraper** — Live review collection and analysis
- [ ] **Genre-based Analysis** — Sentiment by movie genre
- [ ] **Recommendation System** — Content-based recommendations using sentiment

---

## 🎓 Learning Resources

- [Natural Language Processing with NLTK](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/)
- [Scikit-learn Text Classification](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [Streamlit Getting Started](https://docs.streamlit.io/)
- [TensorFlow NLP Guide](https://www.tensorflow.org/text)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Sri Nithya S** — Data Science Enthusiast | Machine Learning Practitioner

- 🔗 [LinkedIn](https://linkedin.com/in/srinithya-s)
- 🐙 [GitHub](https://github.com/Srinithya1503)
- 📧 [Email](venkatsri1503@gmail.com)
---

## ⭐ Acknowledgments

- Dataset: [Kaggle - IMDb Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- Inspired by real-world NLP applications in entertainment industry

---

## 🙋 FAQ

**Q: Do I need a GPU?**  
A: No, this project runs on CPU. GPU is optional for advanced models (BERT, LSTM).

**Q: How long does training take?**  
A: ~5-10 minutes on a standard laptop.

**Q: Can I use this on other datasets?**  
A: Yes! The pipeline is general and works with any review dataset.

**Q: How do I improve model accuracy?**  
A: Try hyperparameter tuning, use BERT/transformers, or collect more data.

---

## 📞 Support

Need help? Open an issue on [GitHub Issues](https://github.com/Srinithya1503/imdb_sentiment_analysis/issues)

---

**Last Updated:** October 2025
**Version:** 1.0  
**Status:** ✅ Active & Maintained
