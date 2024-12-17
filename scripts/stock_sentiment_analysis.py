import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def process_stock_sentiment_correlation(stock_data_folder, news_data):
    """
    Processes all stock CSV files in a folder, merges with news sentiment data,
    computes correlation, and generates scatter plots.

    Parameters:
    - stock_data_folder (str): Path to the folder containing stock CSV files.
    - news_data (pd.DataFrame): DataFrame containing the news sentiment data.
    """
    for filename in os.listdir(stock_data_folder):
        if filename.endswith('.csv'):
            # Load stock data
            stock_file_path = os.path.join(stock_data_folder, filename)
            stock_data = pd.read_csv(stock_file_path)
            stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce').dt.date
            stock_data = stock_data.dropna(subset=['Date'])
            
            # Merge stock and aggregated sentiment data
            aligned_data = pd.merge(stock_data, news_data, left_on='Date', right_on='date', how='inner')
            
            # Compute daily stock returns
            aligned_data['stock_return'] = aligned_data['Close'].pct_change() * 100
            aligned_data = aligned_data.dropna(subset=['stock_return', 'sentiment_score'])
            
            # Calculate correlation
            correlation = aligned_data[['stock_return', 'sentiment_score']].corr().iloc[0, 1]
            print(f"Correlation for {filename}: {correlation}")
            
            # Scatterplot: Sentiment Score vs Stock Return
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x='sentiment_score', y='stock_return', data=aligned_data)
            plt.title(f"Sentiment vs. Stock Returns for {filename}")
            plt.xlabel("Sentiment Score")
            plt.ylabel("Stock Return (%)")
            plt.show()
