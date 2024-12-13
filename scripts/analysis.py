# Add a column for headline lengths
def stat(d):
    d['headline_length'] = d['headline'].str.len()

    # Basic statistics
    headline_stats = d['headline_length'].describe()
    print("Headline Length Statistics:")
    print(headline_stats)

    # Visualize the distribution
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.histplot(d['headline_length'], bins=30, kde=True)
    plt.title("Distribution of Headline Lengths")
    plt.xlabel("Headline Length")
    plt.ylabel("Frequency")
    plt.show()
