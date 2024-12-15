import pandas as pd
import pynance.tech as tech
import os
import matplotlib.pyplot as plt
import seaborn as sns
# Step 1: Define the path to the data folder
# data_folder = '../data/yfinance_data/'  # Replace with the actual path to your data
def load_and_process_stock_data(data_folder):
# Step 2: List all the stock files
    stock_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]

    # Step 3: Dictionary to store DataFrames for each stock
    stock_data = {}

    # Step 4: Load and prepare the data
    for file in stock_files:
        stock_name = file.split('_')[0]  # Extract stock name from file name
        file_path = os.path.join(data_folder, file)
        
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Check if required columns are present
        required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        if all(column in df.columns for column in required_columns):
            # Convert 'Date' column to datetime
            df['Date'] = pd.to_datetime(df['Date'])
            
            # Sort data by date
            df = df.sort_values('Date')
            
            # Step 5: Add financial indicators using the pynance library
            print(f"Applying indicators to {stock_name}...")

            # Calculate the Simple Moving Average (SMA)
            df['SMA'] = tech.sma(df['Close'], length=14)  # 14-period SMA

            # Calculate the Exponential Moving Average (EMA)
            df['EMA'] = tech.ema(df['Close'], length=14)  # 14-period EMA

            # Calculate Volatility (standard deviation of the closing prices)
            df['Volatility'] = tech.volatility(df['Close'], length=14)

            # Store the processed data in the dictionary
            stock_data[stock_name] = df

            # Print the last few rows to confirm the calculations
            # print(df[['Date', 'Close', 'SMA', 'EMA', 'Volatility']].tail())
    return stock_data
def visualize_stock_data(stock_data):
        for stock, df in stock_data.items(): 
            print(f"\n{stock} data with indicators:")
            print(df[['Date', 'Close', 'SMA', 'EMA', 'Volatility']].tail())
        # print(df[['Date', 'Close', 'SMA_10', 'SMA_20', 'RSI', 'MACD', 'MACD_Signal', 'MACD_Hist']].tail())
            # Step 6: Visualizing the data
            plt.figure(figsize=(12, 8))

            # Plot the stock price (Close) along with the SMA and EMA
            plt.subplot(2, 2, 1)
            plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
            plt.plot(df['Date'], df['SMA'], label='14-period SMA', color='orange')
            plt.plot(df['Date'], df['EMA'], label='14-period EMA', color='green')
            plt.title(f'{stock} Stock Price with SMA and EMA')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()

            # Plot the Volatility
            plt.subplot(2, 2, 2)
            plt.plot(df['Date'], df['Volatility'], label='Volatility', color='red')
            plt.title(f'{stock} Volatility')
            plt.xlabel('Date')
            plt.ylabel('Volatility')
            plt.legend()

            plt.tight_layout()
            plt.show()

            # Optional: Save the processed data to a new CSV file
            # df.to_csv(f'processed_{stock_name}.csv', index=False)

    # If needed, access data for a specific stock by name:
    # specific_stock_data = stock_data['AAPL']  # Example for Apple
