# 🚀 Complete Setup Guide - IMDb Sentiment Analysis

Follow this step-by-step guide to set up and run the project.

---

## ⏱️ Estimated Setup Time: 15-20 minutes

---

## 📋 Prerequisites

Before starting, ensure you have:

- ✅ Python 3.8 or higher
- ✅ Git installed
- ✅ ~2GB free disk space
- ✅ Terminal/Command Prompt access
- ✅ Kaggle account (for dataset download)

**Check Python version:**
```bash
python --version
# Should show Python 3.8.0 or higher
```

---

## 🎯 Step-by-Step Installation

### **Step 1: Clone the Repository**

```bash
# Clone the project
git clone https://github.com/yourusername/imdb_sentiment_analysis.git

# Navigate to project directory
cd imdb_sentiment_analysis

# Verify structure
ls -la
# Should see: README.md, requirements.txt, .gitignore, src/, data/, notebooks/, etc.
```

---

### **Step 2: Create Virtual Environment**

A virtual environment isolates project dependencies from your system Python.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Verify activation:**
```bash
# Should show (venv) prefix in terminal
python --version
```

---

### **Step 3: Install Python Dependencies**

```bash
# Upgrade pip (important for smooth installation)
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

**This will install:**
- Data processing: pandas, numpy
- NLP: nltk, spacy
- ML: scikit-learn
- Visualization: matplotlib, seaborn, wordcloud
- Dashboard: streamlit
- And more...

**Verify installation:**
```bash
python -c "import pandas; import sklearn; print('✓ All packages installed!')"
```

---

### **Step 4: Download NLP Models**

```bash
# Download NLTK data
python -m nltk.downloader stopwords punkt wordnet

# Download spaCy model
python -m spacy download en_core_web_sm
```

**What this downloads:**
- NLTK: Stopwords, tokenizers, wordnet lemmatizer
- spaCy: English language model for better NLP

---

### **Step 5: Download IMDb Dataset**

#### Option A: Manual Download (Recommended)

1. Visit: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
2. Click "Download" button
3. Wait for `imdb_dataset.csv` to download
4. Extract and place in `data/raw/` folder:
   ```
   imdb_sentiment_analysis/
   └── data/
       └── raw/
           └── imdb_dataset.csv  ← Place here
   ```

#### Option B: Kaggle API (Advanced)

```bash
# Install Kaggle CLI
pip install kaggle

# Setup API credentials
# Download from: https://www.kaggle.com/settings/account
# Copy kaggle.json to ~/.kaggle/

# Download dataset
kaggle datasets download -d lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
unzip imdb-dataset-of-50k-movie-reviews.zip -d data/raw/
```

**Verify dataset:**
```bash
ls -lh data/raw/imdb_dataset.csv
# Should show ~130 MB file
```

---

### **Step 6: Verify Project Structure**

```bash
# Create directory structure if needed
mkdir -p data/raw data/processed notebooks models outputs/visualizations outputs/results

# Verify structure
tree . -I 'venv|__pycache__'
# Or: ls -la data/ src/ models/ outputs/
```

**Expected structure:**
```
imdb_sentiment_analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── sentiment_analysis.py
├── app.py
├── data/
│   ├── raw/
│   │   └── imdb_dataset.csv      ✓ Downloaded
│   ├── processed/
│   └── README.md
├── src/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── modeling.py
│   └── utils.py
├── notebooks/
│   └── sentiment_analysis.ipynb
├── models/                        (will be created)
└── outputs/                       (will be created)
```

---

## ▶️ Running the Project

### **Option 1: Run Main Pipeline (Recommended First)**

This trains models and generates visualizations.

```bash
# Make sure virtual environment is active
python sentiment_analysis.py
```

**What it does:**
1. ✅ Loads 50K reviews
2. ✅ Analyzes data (EDA)
3. ✅ Generates visualizations
4. ✅ Cleans and preprocesses text
5. ✅ Trains 3 ML models
6. ✅ Evaluates performance
7. ✅ Saves models to `models/`
8. ✅ Saves results to `outputs/`

**Expected output:**
```
🎬  IMDb MOVIE REVIEWS SENTIMENT ANALYSIS  🎬
============================================

Step 1: Setting Up Directories
✓ Directories created/verified

Step 2: Loading Data
✓ Successfully loaded: data/raw/imdb_dataset.csv
  • Total reviews: 50,000
  
Step 3: Data Validation
✓ Data validation passed

...

[Process continues for 5-10 minutes]

PIPELINE COMPLETE! ✅
```

**Expected runtime:** 5-15 minutes (depending on CPU)

---

### **Option 2: Launch Interactive Dashboard**

After running the pipeline, launch the Streamlit dashboard:

```bash
streamlit run app.py
```

**Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**Open in browser:** http://localhost:8501

**Features:**
- 🔮 Real-time sentiment prediction
- 📊 Model performance statistics
- 🎨 Interactive visualizations
- ⚖️ Compare all 3 models
- 📖 About section

---

### **Option 3: Interactive Jupyter Notebook**

For experimentation and learning:

```bash
jupyter notebook notebooks/sentiment_analysis.ipynb
```

**Features:**
- Step-by-step code execution
- Interactive visualizations
- Custom experiments
- Learning-friendly environment

---

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Virtual environment activated: `(venv)` shown in terminal
- [ ] Python packages installed: `pip list` shows all requirements
- [ ] NLP models downloaded: Can import nltk and spacy
- [ ] Dataset downloaded: `data/raw/imdb_dataset.csv` exists (~130 MB)
- [ ] Project structure created: All directories exist
- [ ] Main pipeline runs: `python sentiment_analysis.py` completes
- [ ] Models generated: Files in `models/` directory
- [ ] Dashboard launches: `streamlit run app.py` opens browser
- [ ] Visualizations created: PNG files in `outputs/visualizations/`
- [ ] Results saved: CSV files in `outputs/results/`

---

## 🔧 Troubleshooting

### Issue: Python not found

**Solution:**
```bash
# Use python3 instead
python3 --version
python3 -m venv venv
python3 sentiment_analysis.py
```

### Issue: Virtual environment not activating

**Windows:**
```bash
# Try alternative activation
venv\Scripts\activate.bat  # or .ps1 for PowerShell
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Issue: "ModuleNotFoundError: No module named..."

**Solution:**
```bash
# Make sure venv is activated
pip install -r requirements.txt
```

### Issue: NLTK data not found

**Solution:**
```bash
python -m nltk.downloader stopwords punkt wordnet
```

### Issue: spaCy model not found

**Solution:**
```bash
python -m spacy download en_core_web_sm
```

### Issue: Dataset file not found

**Solution:**
```bash
# Verify file exists
ls -l data/raw/imdb_dataset.csv

# If not found, download from Kaggle
# https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
```

### Issue: Out of memory error

**Solution:**
```python
# Edit sentiment_analysis.py
# Change: SAMPLE_SIZE = None
# To: SAMPLE_SIZE = 5000  # Use 5000 reviews instead of 50000
```

### Issue: Slow performance

**Solution:**
```python
# Edit sentiment_analysis.py
# Use smaller dataset for testing:
SAMPLE_SIZE = 1000

# Or reduce features:
MAX_FEATURES = 2000  # Instead of 5000
```

### Issue: Port 8501 already in use (Streamlit)

**Solution:**
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

### Issue: Models not loading in Streamlit

**Solution:**
```bash
# Ensure pipeline was run first
python sentiment_analysis.py

# Verify model files exist
ls -la models/*.pkl
```

---

## 📚 Next Steps After Setup

### 1. Explore the Data
```bash
jupyter notebook notebooks/sentiment_analysis.ipynb
```

### 2. Make Predictions
```bash
streamlit run app.py
# Use the web interface to test predictions
```

### 3. Understand the Code
- Read `README.md` for high-level overview
- Review `src/preprocessing.py` to understand text cleaning
- Check `src/modeling.py` to see model training logic
- Study `sentiment_analysis.py` for complete workflow

### 4. Experiment
- Modify preprocessing steps
- Try different hyperparameters
- Add new models (e.g., Random Forest, Gradient Boosting)
- Implement aspect-based sentiment analysis

### 5. Deploy
- Package as Flask REST API
- Deploy to AWS/Heroku/Google Cloud
- Create Docker container
- Package as Python package for PyPI

---

## 🎓 Learning Resources

- **NLTK Tutorial:** https://www.nltk.org/howto
- **spaCy Guide:** https://spacy.io/usage
- **scikit-learn ML:** https://scikit-learn.org/stable/
- **Streamlit Docs:** https://docs.streamlit.io/
- **NLP Course:** https://www.fast.ai/

---

## 📞 Getting Help

If you encounter issues:

1. **Check the FAQ** in README.md
2. **Review troubleshooting** section above
3. **Search GitHub Issues:** https://github.com/yourusername/imdb_sentiment_analysis/issues
4. **Ask on Stack Overflow:** Tag your question with `nlp`, `sentiment-analysis`, `scikit-learn`
5. **Contact author** (links in README.md)

---

## 🎉 Success!

Congratulations! You've successfully set up the IMDb Sentiment Analysis project.

**You can now:**
- ✅ Run the complete ML pipeline
- ✅ Train sentiment classification models
- ✅ Make predictions on new reviews
- ✅ Explore interactive dashboard
- ✅ Analyze results and visualizations

**Happy learning! 🚀**