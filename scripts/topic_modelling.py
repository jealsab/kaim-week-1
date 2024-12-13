    
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import string
# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
def common_words(d):

    # Load the data from the CSV file into a Pandas DataFrame
   

    # Tokenize and preprocess the text data (headlines)
    def preprocess_text(text):
        # Tokenization and lowercasing
        tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
        # Remove punctuation and non-alphabetic tokens
        tokens = [word for word in tokens if word.isalpha()]
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        return ' '.join(tokens)

    # Apply preprocessing to all headlines
    d['processed_headline'] = d['headline'].apply(preprocess_text)

    # Vectorize the processed headlines using TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)  # You can change the number of features (words)
    X = vectorizer.fit_transform(d['processed_headline'])

    # Apply LDA for topic modeling
    n_topics = 5  # Number of topics you want to extract
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)

    # Display the top words for each topic
    n_words = 10  # Number of words to display for each topic
    for idx, topic in enumerate(lda.components_):
        print(f"Topic {idx + 1}:")
        top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-n_words:]]
        print(' '.join(top_words))
        print()

    # Optionally: To get the distribution of topics per document (article)
    topic_distribution = lda.transform(X)