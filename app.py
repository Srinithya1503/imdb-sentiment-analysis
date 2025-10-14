"""
================================================================================
Streamlit Dashboard - IMDb Sentiment Analysis
================================================================================

Interactive web application for sentiment prediction and model visualization.

Run: streamlit run app.py
Visit: http://localhost:8501
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from src.preprocessing import preprocess_text
import plotly.express as px
import plotly.graph_objects as go

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="IMDb Sentiment Analyzer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# LOAD MODELS & VECTORIZER
# ============================================================================

@st.cache_resource
def load_models():
    """Load trained models and vectorizer from pickle files"""
    try:
        vectorizer = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
        models = {
            'Logistic Regression': pickle.load(open('models/logistic_regression.pkl', 'rb')),
            'Naive Bayes': pickle.load(open('models/naive_bayes.pkl', 'rb')),
            'SVM': pickle.load(open('models/svm_model.pkl', 'rb'))
        }
        return vectorizer, models
    except FileNotFoundError as e:
        st.error(f"❌ Error loading models: {e}")
        st.info("Please run: python sentiment_analysis.py")
        st.stop()

vectorizer, models = load_models()

# ============================================================================
# HEADER & TITLE
# ============================================================================

st.title("🎬 IMDb Movie Review Sentiment Analyzer")
st.markdown("Predict sentiment (positive/negative) for any movie review in real-time!")

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================

st.sidebar.header("⚙️ Settings")
selected_model = st.sidebar.selectbox(
    "Choose Model",
    list(models.keys()),
    help="Select which model to use for predictions",
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 About This Project")
st.sidebar.markdown("""
- **Dataset:** 50,000 IMDb reviews
- **Models:** Logistic Regression, Naïve Bayes, SVM
- **Features:** TF-IDF vectorization
- **Balanced:** 50% positive, 50% negative
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Links")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.markdown("[📖 Documentation](https://github.com)")
with col2:
    st.markdown("[🐙 GitHub](https://github.com)")

# ============================================================================
# MAIN TABS
# ============================================================================

tab1, tab2, tab3, tab4 = st.tabs(["🔮 Predict", "📊 Statistics", "📈 Model Info", "ℹ️ About"])

# ============================================================================
# TAB 1: PREDICTION
# ============================================================================

with tab1:
    st.subheader("🎯 Analyze Your Movie Review")
    
    # Input area
    user_review = st.text_area(
        "Paste your movie review here:",
        placeholder="e.g., This movie was absolutely amazing! Best film I've ever seen.",
        height=120,
        key="review_input"
    )
    
    # Prediction button
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        predict_button = st.button("🎯 Predict Sentiment", use_container_width=True)
    with col2:
        compare_button = st.button("⚖️ Compare All Models", use_container_width=True)
    
    # Make prediction
    if predict_button and user_review.strip():
        with st.spinner("Analyzing sentiment..."):
            # Preprocess
            cleaned_review = preprocess_text(user_review)
            X_vectorized = vectorizer.transform([cleaned_review])
            
            # Get prediction and confidence
            prediction = models[selected_model].predict(X_vectorized)[0]
            confidence = models[selected_model].predict_proba(X_vectorized).max()
            
            # Display results
            st.success("✅ Analysis Complete!")
            
            col1, col2 = st.columns(2)
            with col1:
                if prediction == 'positive':
                    st.metric(
                        "Sentiment",
                        "✅ POSITIVE",
                        delta="Favorable review"
                    )
                else:
                    st.metric(
                        "Sentiment",
                        "❌ NEGATIVE",
                        delta="Unfavorable review"
                    )
            
            with col2:
                st.metric(
                    "Confidence Score",
                    f"{confidence*100:.1f}%",
                    delta="Model certainty"
                )
            
            st.divider()
            
            # Show preprocessed text
            with st.expander("📝 View Preprocessed Text"):
                st.text(cleaned_review if cleaned_review else "[Empty after preprocessing]")
    
    elif compare_button and user_review.strip():
        with st.spinner("Comparing all models..."):
            # Preprocess
            cleaned_review = preprocess_text(user_review)
            X_vectorized = vectorizer.transform([cleaned_review])
            
            st.success("✅ Comparison Complete!")
            
            # Get predictions from all models
            comparison_data = []
            for model_name, model in models.items():
                pred = model.predict(X_vectorized)[0]
                conf = model.predict_proba(X_vectorized).max()
                comparison_data.append({
                    'Model': model_name,
                    'Prediction': pred,
                    'Confidence': f"{conf*100:.1f}%"
                })
            
            comparison_df = pd.DataFrame(comparison_data)
            st.dataframe(comparison_df, use_container_width=True)
            
            # Visualize predictions
            pred_counts = [comparison_data[i]['Prediction'] for i in range(len(comparison_data))]
            fig = px.bar(
                x=[m['Model'] for m in comparison_data],
                y=[1, 1, 1],
                color=pred_counts,
                color_discrete_map={'positive': '#2ecc71', 'negative': '#e74c3c'},
                title="Model Predictions",
                labels={'y': 'Count', 'x': 'Model'}
            )
            st.plotly_chart(fig, use_container_width=True)
    
    elif predict_button or compare_button:
        st.warning("⚠️ Please enter a review to analyze!")
    
    # Example reviews section
    st.divider()
    st.subheader("📝 Try These Examples")
    
    examples = [
        "Absolutely brilliant! One of the best films ever made. Highly recommend!",
        "Terrible movie. Complete waste of time and money.",
        "It was okay, nothing special but watchable.",
        "Amazing cinematography and outstanding performances!",
        "Boring plot with weak acting. Very disappointing."
    ]
    
    cols = st.columns(2)
    for i, example in enumerate(examples):
        with cols[i % 2]:
            if st.button(f"📌 Example {i+1}", use_container_width=True, key=f"ex_{i}"):
                st.session_state.review_input = example
                st.rerun()

# ============================================================================
# TAB 2: STATISTICS
# ============================================================================

with tab2:
    st.subheader("📊 Model Performance Overview")
    
    # Load performance metrics
    if os.path.exists('outputs/results/model_performance.csv'):
        perf_df = pd.read_csv('outputs/results/model_performance.csv')
        
        # Display metrics table
        st.dataframe(
            perf_df[['Model', 'Accuracy', 'Precision', 'Recall', 'F1-Score']],
            use_container_width=True
        )
        
        # Visualize accuracy comparison
        fig = px.bar(
            perf_df,
            x='Model',
            y=['Accuracy', 'Precision', 'Recall', 'F1-Score'],
            barmode='group',
            title='Model Performance Comparison',
            labels={'value': 'Score', 'variable': 'Metric'}
        )
        fig.update_yaxes(range=[0.8, 1.0])
        st.plotly_chart(fig, use_container_width=True)
        
        # Show best model
        best_idx = perf_df['Accuracy'].idxmax()
        best_model_name = perf_df.loc[best_idx, 'Model']
        best_accuracy = perf_df.loc[best_idx, 'Accuracy']
        
        st.success(f"🏆 **Best Model:** {best_model_name} ({best_accuracy*100:.2f}% accuracy)")
    
    else:
        st.warning("⚠️ No performance data found. Run: python sentiment_analysis.py")
    
    st.divider()
    
    # Display visualizations
    st.subheader("🎨 Visualizations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if os.path.exists('outputs/visualizations/word_clouds.png'):
            st.image(
                'outputs/visualizations/word_clouds.png',
                caption='Word Clouds: Positive vs Negative Reviews',
                use_column_width=True
            )
    
    with col2:
        if os.path.exists('outputs/visualizations/sentiment_distribution.png'):
            st.image(
                'outputs/visualizations/sentiment_distribution.png',
                caption='Sentiment Distribution',
                use_column_width=True
            )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if os.path.exists('outputs/visualizations/review_length_distribution.png'):
            st.image(
                'outputs/visualizations/review_length_distribution.png',
                caption='Review Length Distribution',
                use_column_width=True
            )
    
    with col2:
        if os.path.exists('outputs/visualizations/frequent_words.png'):
            st.image(
                'outputs/visualizations/frequent_words.png',
                caption='Most Frequent Words',
                use_column_width=True
            )

# ============================================================================
# TAB 3: MODEL INFORMATION
# ============================================================================

with tab3:
    st.subheader("🤖 Model Details")
    
    model_info = {
        'Logistic Regression': {
            'description': 'Linear classifier using logistic function',
            'pros': ['Highest accuracy', 'Fast inference', 'Interpretable'],
            'cons': ['Linear boundaries', 'Less flexible'],
            'best_for': 'Production deployments'
        },
        'Naive Bayes': {
            'description': 'Probabilistic classifier based on Bayes theorem',
            'pros': ['Very fast', 'Lightweight', 'Good baseline'],
            'cons': ['Lower accuracy', 'Assumes independence'],
            'best_for': 'Real-time inference'
        },
        'SVM': {
            'description': 'Support Vector Machine with linear kernel',
            'pros': ['Robust', 'Good generalization', 'Handles high dimensions'],
            'cons': ['Slower training', 'Less interpretable'],
            'best_for': 'Complex patterns'
        }
    }
    
    for model_name, info in model_info.items():
        with st.expander(f"📖 {model_name}", expanded=(model_name == 'Logistic Regression')):
            st.markdown(f"**Description:** {info['description']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Pros:**")
                for pro in info['pros']:
                    st.markdown(f"✅ {pro}")
            
            with col2:
                st.markdown("**Cons:**")
                for con in info['cons']:
                    st.markdown(f"⚠️ {con}")
            
            st.markdown(f"**Best For:** {info['best_for']}")

# ============================================================================
# TAB 4: ABOUT
# ============================================================================

with tab4:
    st.subheader("About This Project")
    
    st.markdown("""
    ### 🎬 IMDb Sentiment Analysis
    
    A machine learning project that classifies IMDb movie reviews as **positive** or **negative** 
    using Natural Language Processing (NLP) and supervised learning.
    
    ---
    
    ### 📊 Dataset
    - **50,000 IMDb reviews** (balanced: 25K positive, 25K negative)
    - **Source:** [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
    
    ---
    
    ### 🤖 Models
    Three classification models are implemented:
    
    1. **Logistic Regression** - Best accuracy (89.2%)
    2. **Naïve Bayes** - Fastest inference
    3. **SVM** - Most robust (88.5%)
    
    ---
    
    ### 💡 Business Applications
    - Studios understand audience reactions to films
    - Streaming platforms improve recommendations
    - Marketers track public sentiment in real-time
    - Production teams make data-driven decisions
    
    ---
    
    ### 🛠️ Technology Stack
    - **Python** - Programming language
    - **Pandas/NumPy** - Data processing
    - **NLTK/spaCy** - Natural language processing
    - **Scikit-learn** - Machine learning
    - **Streamlit** - Web dashboard
    - **Plotly** - Interactive visualizations
    
    ---
    
    ### 📚 Key Features
    - ✅ Real-time sentiment prediction
    - ✅ Model comparison interface
    - ✅ Performance metrics visualization
    - ✅ Confidence scores
    - ✅ Text preprocessing pipeline
    
    ---
    
    ### 🔗 Resources
    - [GitHub Repository](https://github.com/yourusername/imdb_sentiment_analysis)
    - [Project Documentation](README.md)
    - [Dataset on Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
    """)

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 0.8em;'>"
    "🎬 IMDb Sentiment Analysis | Built with Streamlit | "
    "<a href='https://github.com'>GitHub</a> | "
    "<a href='https://kaggle.com'>Kaggle</a>"
    "</p>",
    unsafe_allow_html=True
)