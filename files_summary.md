# 📋 IMDb Sentiment Analysis - Complete File Listing

## 📁 Project Structure Overview

This document provides a complete summary of all files in the project.

---

## 🎯 Root Level Files

| File | Purpose | Size | Type |
|------|---------|------|------|
| `README.md` | Main project documentation | ~5 KB | Markdown |
| `requirements.txt` | Python dependencies | ~0.5 KB | Text |
| `.gitignore` | Git ignore patterns | ~2 KB | Text |
| `sentiment_analysis.py` | Main pipeline script | ~15 KB | Python |
| `app.py` | Streamlit dashboard | ~18 KB | Python |

---

## 📂 Directory Structure & Files

### **data/**
Contains all dataset files and data documentation.

```
data/
├── README.md                          # Data directory documentation
├── raw/
│   └── imdb_dataset.csv               # Original 50K reviews (Download from Kaggle)
└── processed/
    └── cleaned_reviews.csv            # Auto-generated preprocessed data
```

**Files:**
- `data/README.md` - Guide for obtaining and understanding datasets
- `data/raw/imdb_dataset.csv` - Original IMDb dataset (⚠️ Not tracked in Git)
- `data/processed/cleaned_reviews.csv` - Generated after running pipeline

---

### **notebooks/**
Interactive Jupyter notebooks for exploration and experimentation.

```
notebooks/
└── sentiment_analysis.ipynb           # Interactive EDA & modeling notebook
```

**File:** `sentiment_analysis.ipynb`
- **Purpose:** Interactive exploration and model experimentation
- **Sections:**
  - Import libraries
  - Load and explore data
  - EDA (visualizations, statistics)
  - Text preprocessing pipeline
  - Feature engineering (TF-IDF)
  - Model training comparison
  - Evaluation and metrics
  - Custom predictions
  - Business insights
- **How to Run:** `jupyter notebook notebooks/sentiment_analysis.ipynb`

---

### **src/**
Core Python modules containing reusable functions.

```
src/
├── __init__.py                        # Package initialization
├── preprocessing.py                   # Text preprocessing functions
├── eda.py                             # Exploratory data analysis
├── modeling.py                        # Model training & evaluation
└── utils.py                           # Helper utilities
```

#### **src/__init__.py** - Package Initialization
- **Purpose:** Makes src/ a Python package; imports key functions
- **Exports:** All public functions from other modules
- **Size:** ~1 KB

#### **src/preprocessing.py** - Text Preprocessing Functions
- **Purpose:** Text cleaning and preparation for modeling
- **Key Functions:**
  - `preprocess_text(text)` - Complete preprocessing pipeline
  - `remove_html_tags(text)` - Remove HTML markup
  - `remove_urls(text)` - Remove URLs from text
  - `remove_contractions(text)` - Expand contractions (don't → do not)
  - `remove_emojis(text)` - Remove emoji characters
  - `clean_dataset(df)` - Apply preprocessing to entire DataFrame
- **Preprocessing Steps:**
  1. Remove HTML tags
  2. Convert to lowercase
  3. Remove URLs
  4. Remove special characters
  5. Tokenization
  6. Stopword removal
  7. Lemmatization
- **Size:** ~4 KB

#### **src/eda.py** - Exploratory Data Analysis Functions
- **Purpose:** Data visualization and analysis
- **Key Functions:**
  - `generate_visualizations(df)` - Create all visualizations
  - `create_word_clouds(df)` - Generate word clouds (positive/negative)
  - `create_sentiment_distribution(df)` - Pie and bar charts
  - `create_review_length_distribution(df)` - Length analysis
  - `create_most_frequent_words(df)` - Top words visualization
  - `analyze_sentiment_distribution(df)` - Print statistics
  - `get_text_statistics(df)` - Calculate text metrics
- **Output:** PNG files saved to `outputs/visualizations/`
- **Size:** ~5 KB

#### **src/modeling.py** - Model Training & Evaluation
- **Purpose:** Train, evaluate, and save ML models
- **Key Functions:**
  - `train_models(X_train, y_train)` - Train 3 models
  - `evaluate_models(models, vectorizer, X_test, y_test)` - Evaluate performance
  - `generate_confusion_matrix(y_test, y_pred)` - Confusion matrix visualization
  - `save_models(models)` - Save to pickle files
  - `load_model(model_name)` - Load trained model
  - `load_vectorizer()` - Load TF-IDF vectorizer
  - `predict_sentiment(review, model, vectorizer)` - Make predictions
- **Models Trained:** Logistic Regression, Naïve Bayes, SVM
- **Size:** ~8 KB

#### **src/utils.py** - Helper Utilities
- **Purpose:** General utility functions
- **Key Functions:**
  - `print_section(title)` - Formatted section headers
  - `print_success(message)` - Success messages
  - `print_error(message)` - Error messages
  - `print_warning(message)` - Warning messages
  - `create_output_directories(dirs)` - Create folders
  - `save_dataframe_to_csv(df, path)` - Save CSV
  - `load_dataframe_from_csv(path)` - Load CSV
  - `calculate_metrics(y_true, y_pred)` - Compute metrics
  - `batch_predict(reviews, model, vectorizer)` - Predict multiple reviews
  - `validate_dataset(df)` - Check data quality
  - `print_progress_bar(current, total)` - Progress indicator
- **Size:** ~6 KB

---

### **models/**
Trained model files and vectorizer.

```
models/
├── README.md                          # Model documentation & usage guide
├── logistic_regression.pkl            # Trained Logistic Regression
├── naive_bayes.pkl                    # Trained Naïve Bayes
├── svm_model.pkl                      # Trained Linear SVM
└── tfidf_vectorizer.pkl               # TF-IDF vectorizer
```

**Files:**
- `models/README.md` - Model loading guide, performance metrics, deployment options
- `models/logistic_regression.pkl` - Best model (89.2% accuracy)
- `models/naive_bayes.pkl` - Fast inference model (86.5% accuracy)
- `models/svm_model.pkl` - Robust model (88.5% accuracy)
- `models/tfidf_vectorizer.pkl` - Feature vectorizer (MUST load before models)

**Note:** These files are auto-generated by running `sentiment_analysis.py`

---

### **outputs/**
Generated results, visualizations, and metrics.

```
outputs/
├── visualizations/
│   ├── word_clouds.png                # Word clouds (positive vs negative)
│   ├── sentiment_distribution.png     # Sentiment pie/bar chart
│   ├── review_length_distribution.png # Review length analysis
│   ├── frequent_words.png             # Top words by sentiment
│   ├── logistic_regression_confusion_matrix.png
│   ├── naive_bayes_confusion_matrix.png
│   └── svm_confusion_matrix.png
└── results/
    ├── model_performance.csv          # Model metrics table
    └── pipeline_summary.txt           # Pipeline execution summary
```

**Files Generated:**
- `outputs/visualizations/` - PNG charts and graphs
- `outputs/results/model_performance.csv` - Accuracy, precision, recall, F1-score
- `outputs/results/pipeline_summary.txt` - Execution summary

**Note:** All files auto-generated by pipeline

---

## 🚀 How Files Work Together

### Execution Flow

```
1. User runs: python sentiment_analysis.py
   │
   ├─→ Load data from: data/raw/imdb_dataset.csv
   │
   ├─→ Use functions from: src/preprocessing.py, src/eda.py, src/utils.py
   │
   ├─→ Preprocess text and save to: data/processed/cleaned_reviews.csv
   │
   ├─→ Create visualizations saved to: outputs/visualizations/
   │
   ├─→ Train models using: src/modeling.py
   │
   ├─→ Save models to: models/*.pkl
   │
   ├─→ Save results to: outputs/results/model_performance.csv
   │
   └─→ Print summary and next steps
```

### Usage Flow

```
1. User runs: streamlit run app.py
   │
   ├─→ Load models from: models/*.pkl
   │
   ├─→ Use vectorizer from: models/tfidf_vectorizer.pkl
   │
   ├─→ Preprocess input using: src/preprocessing.py
   │
   ├─→ Make predictions with loaded models
   │
   ├─→ Display results in: app.py (Streamlit UI)
   │
   └─→ Show visualizations from: outputs/visualizations/
```

---

## 📊 File Statistics

| Category | Count | Total Size |
|----------|-------|-----------|
| Python Scripts | 6 | ~50 KB |
| Markdown Docs | 3 | ~20 KB |
| Data Files | 2 | ~150 MB* |
| Model Files | 4 | ~22 MB* |
| Visualizations | 7 | ~15 MB* |
| Results | 2 | ~50 KB |

*Generated files (not in Git)

---

## 🔄 File Dependencies

### preprocessing.py
- Depends on: NLTK, spaCy
- Used by: sentiment_analysis.py, modeling.py, app.py

### eda.py
- Depends on: pandas, matplotlib, seaborn, wordcloud
- Used by: sentiment_analysis.py

### modeling.py
- Depends on: scikit-learn, pandas
- Uses: preprocessing.py
- Used by: sentiment_analysis.py, app.py

### utils.py
- Depends on: pandas, scikit-learn
- Used by: All modules

### sentiment_analysis.py
- Depends on: All src modules
- Input: data/raw/imdb_dataset.csv
- Output: models/, outputs/

### app.py
- Depends on: src.preprocessing, src.modeling
- Input: models/, outputs/
- Output: Web dashboard (Streamlit)

---

## 📝 File Editing Guide

### What to Modify

**Configuration Changes:**
- Edit `sentiment_analysis.py` top section:
  - Change `TEST_SIZE`, `MAX_FEATURES`, `RANDOM_STATE`
  - Modify `SAMPLE_SIZE` to use smaller dataset

**Add New Models:**
- Edit `src/modeling.py` in `train_models()` function
- Add new model instantiation and training

**Change Preprocessing:**
- Edit `src/preprocessing.py` in `preprocess_text()` function
- Add/remove preprocessing steps

**Customize Dashboard:**
- Edit `app.py` to modify UI, colors, layout
- Change sections, titles, or add new features

### What NOT to Modify

- Model pickle files (delete and retrain if needed)
- Generated CSV files (auto-generated)
- Generated visualizations (auto-generated)

---

## ✅ Checklist: Files to Create

When setting up the project, create these directories and files:

```
□ Create data/raw/          (place imdb_dataset.csv here)
□ Create data/processed/    (auto-created by script)
□ Create notebooks/         (for Jupyter exploration)
□ Create src/               (with all .py modules)
□ Create models/            (auto-created by training)
□ Create outputs/           (auto-created by pipeline)
□ Copy sentiment_analysis.py to root
□ Copy app.py to root
□ Copy requirements.txt to root
□ Copy .gitignore to root
```

---

## 🎯 Quick Reference

### Run Main Pipeline
```bash
python sentiment_analysis.py
```
**Generates:** Models, visualizations, results

### Launch Dashboard
```bash
streamlit run app.py
```
**Requires:** Pre-trained models in models/ folder

### Open Notebook
```bash
jupyter notebook notebooks/sentiment_analysis.ipynb
```
**For:** Interactive exploration and experimentation

### Install Dependencies
```bash
pip install -r requirements.txt
```
**First Time:** After cloning project

---

## 📞 File-Related Issues

| Problem | Solution |
|---------|----------|
| `FileNotFoundError: imdb_dataset.csv` | Download from Kaggle, place in data/raw/ |
| `ModuleNotFoundError: src` | Ensure src/ folder exists in project root |
| Models not loading | Run: `python sentiment_analysis.py` first |
| Streamlit won't start | Check models/ folder exists and has .pkl files |
| Missing visualizations | Run: `python sentiment_analysis.py` to generate |

---

## 📄 Summary

**Total Files:** 20+
**Total Lines of Code:** ~1,500
**Documentation:** ~30 pages
**Time to Setup:** ~10 minutes

**Key Files to Remember:**
1. `sentiment_analysis.py` - Run this first
2. `app.py` - Run this second (dashboard)
3. `src/preprocessing.py` - Core preprocessing logic
4. `models/` - Where trained models live
5. `data/raw/imdb_dataset.csv` - Download this from Kaggle