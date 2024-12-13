def pub_freq(d):
    # time analysis
# data=pd.read_csv(file_path)
# print(data.columns)
    d['date'] = pd.to_datetime(d['date'], utc=True)  # Convert to offset-aware datetime in UTC
    d.set_index('date', inplace=True)
    # Resample to count articles published per day
    daily_counts = d['headline'].resample('D').count()

    # Plot daily publication frequency
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    plt.title("Daily Publication Frequency")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.grid()
    plt.show()

    d['hour'] = d.index.hour

    # Group by hour to find the frequency of publications
    hourly_distribution = d['hour'].value_counts().sort_index()

    # Plot the distribution of publication times
    plt.figure(figsize=(12, 6))
    hourly_distribution.plot(kind='bar', color='skyblue')
    plt.title("Publication Frequency by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Articles")
    plt.grid()
    plt.show()

    # Annotate spikes in daily publication frequency
    spikes = daily_counts[daily_counts > daily_counts.mean() + 2 * daily_counts.std()]  # Example threshold
    plt.figure(figsize=(12, 6))
    daily_counts.plot()
    for date, count in spikes.items():
        plt.text(date, count, str(count), color='red', fontsize=9)
    plt.title("Daily Publication Frequency with Spikes Highlighted")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.grid()
    plt.show()
    # from where is the xlabel of the monthly publication frquency 