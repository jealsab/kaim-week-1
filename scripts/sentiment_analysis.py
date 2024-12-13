# scripts/sentiment_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

def analyze_and_visualize_sentiment(d):
    """
    Analyzes the sentiment of headlines in the DataFrame and visualizes the results.

    Parameters:
    data (DataFrame): The DataFrame containing the 'headline' column.

    Returns:
    None
    """
    # Ensure the VADER lexicon is downloaded
    nltk.download('vader_lexicon', quiet=True)

    # Initialize Sentiment Analyzer
    sid = SentimentIntensityAnalyzer()

    # Function to analyze sentiment
    def analyze_sentiment(p):
        scores = sid.polarity_scores(p)  # Get sentiment scores
        # Determine sentiment based on compound score
        if scores['compound'] > 0.05:
            return 'Positive'
        elif scores['compound'] < -0.05:
            return 'Negative'
        else:
            return 'Neutral'

    # Apply the function directly to the 'headline' column
    d['Sentiment'] = d['headline'].apply(analyze_sentiment)

    # Visualize the sentiment distribution
    plt.figure(figsize=(8, 5))
    d['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title('Sentiment Analysis of Headlines')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.show()