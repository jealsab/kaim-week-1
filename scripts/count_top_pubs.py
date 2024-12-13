# Count articles per publisher
import matplotlib.pyplot as plt
def count_top_publishers(d):
    publisher_counts = d['publisher'].value_counts()
    print("Number of Articles Per Publisher:")
    print(publisher_counts)

    # Visualize the most active publishers
    top_publishers = publisher_counts.head(10)  # Top 10 publishers
    top_publishers.plot(kind='bar', figsize=(10, 6))
    plt.title("Top 10 Most Active Publishers")
    plt.xlabel("Publisher")
    plt.ylabel("Number of Articles")
    plt.show()