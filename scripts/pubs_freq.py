import pandas as pd
import matplotlib.pyplot as plt
def pub_fre(d):

    # Load the data from the CSV file into a Pandas DataFrame

    # Convert the 'date' column to datetime (if not already in datetime format)
    d['date'] = pd.to_datetime(d['date'], utc=True)

    # Set the 'date' column as the index
    d.set_index('date', inplace=True)

    # Resample the data by day (you can adjust to 'H' for hourly, 'W' for weekly, etc.)
    publication_freq = d.resample('D').size()  # Daily frequency

    # Descriptive statistics
    desc_stats = publication_freq.describe()
    print("Descriptive Statistics:")
    print(desc_stats)

    # Plot the publication frequency over time
    plt.figure(figsize=(10, 6))
    plt.plot(publication_freq.index, publication_freq.values, marker='o', linestyle='-', color='b')
    plt.title('Publication Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles Published')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    # Analyze spikes or periods of increased publication frequency
    # Identify when there's a spike, e.g., if the frequency is higher than the moving average
    moving_avg = publication_freq.rolling(window=7).mean()  # 7-day moving average for smoother visualization

    # Plot with moving average to highlight spikes
    plt.figure(figsize=(10, 6))
    plt.plot(publication_freq.index, publication_freq.values, marker='o', linestyle='-', label='Publication Frequency', color='b')
    plt.plot(moving_avg.index, moving_avg.values, label='7-Day Moving Average', color='r', linewidth=2)
    plt.title('Publication Frequency with Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles Published')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.show()

    # Optionally: Identify significant dates or periods with unusually high publication frequency
    threshold = 10  # Set a threshold for what constitutes a "spike"
    spikes = publication_freq[publication_freq > threshold]
    print("Spikes in publication frequency detected on:")
    print(spikes)
