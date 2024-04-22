import nltk
nltk.download('stopwords')

import re
from collections import Counter
from nltk.corpus import stopwords
import nltk
import os

# Initialize NLTK
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Load NLTK stopwords
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(text):
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Function to count word frequency
def count_word_frequency(text):
    words = text.split()
    return Counter(words)

# Read contents of the file
file_path = "C:/Users/Data/Desktop/cloud_Assignment/paragraphs.txt"
if os.path.isfile(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
else:
    print(f"File '{file_path}' not found.")
    exit()

# Preprocess text
processed_text = preprocess_text(content)

# Count word frequency
word_frequency = count_word_frequency(processed_text)

# Display word frequency count
for word, count in word_frequency.items():
    print(f'{word}: {count}')

