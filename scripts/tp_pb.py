import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def anlyze_publishers(d):
    """
    Cleans the 'publisher' column to extract domains from emails,
    identifies the top publishers, and visualizes the results.

    Parameters:
    data (DataFrame): The DataFrame containing the 'publisher' column.

    Returns:
    None
    """
    # Clean the 'publisher' column to extract domains from emails
    def clean_publisher_name(name):
        if '@' in name:
            domain = name.split('@')[1].split('.')[0]  # Extract domain
            return domain
        return name  # Return name as-is if it doesn't contain an email
    
    # Apply the cleaning function
    d['cleaned_publisher'] = d['publisher'].apply(clean_publisher_name)

    # Identify top publishers overall
    top_publishers = d['cleaned_publisher'].value_counts().head(10)
    print("Top 10 Publishers by Number of Articles:")
    print(top_publishers)

    # Plot top publishers
    plt.figure(figsize=(12, 6))
    top_publishers.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Publishers by Number of Articles')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.show()

# Example usage (uncomment to use with your DataFrame)
# data = pd.read_csv('your_file.csv')
# analyze_publishers(data)