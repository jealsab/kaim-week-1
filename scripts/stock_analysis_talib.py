# stock_analysis.py
import pandas as pd
import talib
import os
import matplotlib.pyplot as plt
def visualize_stock_data(stock_data): 
    for stock, df in stock_data.items(): 
        print(f"\n{stock} data with indicators:")
        print(df[['Date', 'Close', 'SMA_10', 'SMA_20', 'RSI', 'MACD', 'MACD_Signal', 'MACD_Hist']].tail())

        # Create a 2x2 grid for subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle(f'{stock} Stock Data and Indicators', fontsize=16)

        # Plot 1: Closing price with SMA_10 and SMA_20
        axes[0, 0].plot(df['Date'], df['Close'], label='Close Price', color='blue', linewidth=1)
        axes[0, 0].plot(df['Date'], df['SMA_10'], label='10-day SMA', color='red', linestyle='--')
        axes[0, 0].plot(df['Date'], df['SMA_20'], label='20-day SMA', color='green', linestyle='--')
        axes[0, 0].set_title('Stock Price and SMAs')
        axes[0, 0].set_xlabel('Date')
        axes[0, 0].set_ylabel('Price')
        axes[0, 0].legend(loc='best')

        # Plot 2: Relative Strength Index (RSI)
        axes[0, 1].plot(df['Date'], df['RSI'], label='14-day RSI', color='orange')
        axes[0, 1].axhline(70, color='red', linestyle='--', label='Overbought (70)')
        axes[0, 1].axhline(30, color='green', linestyle='--', label='Oversold (30)')
        axes[0, 1].set_title('RSI')
        axes[0, 1].set_xlabel('Date')
        axes[0, 1].set_ylabel('RSI Value')
        axes[0, 1].legend(loc='best')

        # Plot 3: MACD and MACD Signal Line
        axes[1, 0].plot(df['Date'], df['MACD'], label='MACD', color='purple')
        axes[1, 0].plot(df['Date'], df['MACD_Signal'], label='MACD Signal', color='red')
        axes[1, 0].set_title('MACD and Signal Line')
        axes[1, 0].set_xlabel('Date')
        axes[1, 0].set_ylabel('MACD Value')
        axes[1, 0].legend(loc='best')

        # Plot 4: MACD Histogram
        axes[1, 1].bar(df['Date'], df['MACD_Hist'], label='MACD Histogram', color='lightblue')
        axes[1, 1].set_title('MACD Histogram')
        axes[1, 1].set_xlabel('Date')
        axes[1, 1].set_ylabel('MACD Histogram')

        # Show the plots
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)  # Adjust the top space for the title
        plt.show()
def load_and_process_stock_data(data_folder):
    stock_files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]
    stock_data = {}

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
            
            # Add TA-Lib indicators
            print(f"Applying indicators to {stock_name}...")
            
            # Simple Moving Averages (SMA)
            df['SMA_10'] = talib.SMA(df['Close'], timeperiod=10)  # 10-day SMA
            df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)  # 20-day SMA
            
            # Relative Strength Index (RSI)
            df['RSI'] = talib.RSI(df['Close'], timeperiod=14)  # 14-day RSI
            
            # Moving Average Convergence Divergence (MACD)
            df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = talib.MACD(df['Close'], 
                                                                        fastperiod=12, 
                                                                        slowperiod=26, 
                                                                        signalperiod=9)
            
            # Store cleaned and enriched DataFrame in the dictionary
            stock_data[stock_name] = df
        else:
            print(f"File {file} is missing required columns. Skipping...")

    return stock_data
