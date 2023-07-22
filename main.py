import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn


def preprocess_text(text):
    """Preprocesses the text by tokenizing, removing stopwords, lemmatizing, and filtering non-English words."""
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]  # Filter out non-alphabetic tokens
    tokens = [token for token in tokens if token not in stopwords.words('english')]  # Remove stopwords

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatize tokens

    tokens = [token for token in tokens if wn.synsets(token)]  # Filter out non-English words
    return tokens


def calculate_similarity(tokens1, tokens2):
    """Calculates the similarity between two lists of preprocessed tokens."""
    intersection = len(set(tokens1) & set(tokens2))
    union = len(set(tokens1) | set(tokens2))
    similarity_percentage = (intersection / union) * 100
    return similarity_percentage


def compare_texts(file1, file2):
    """Compares two text files and returns the similarity percentage based on word order and meaning."""
    with open(file1, 'r') as file:
        text1 = file.read()
    with open(file2, 'r') as file:
        text2 = file.read()

    tokens1 = preprocess_text(text1)
    tokens2 = preprocess_text(text2)

    similarity_percentage = calculate_similarity(tokens1, tokens2)
    return similarity_percentage


def check_plagiarism(directory):
    """Checks plagiarism among all text files in a directory."""
    files = os.listdir(directory)

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = os.path.join(directory, files[i])
            file2 = os.path.join(directory, files[j])

            similarity_percentage = compare_texts(file1, file2)
            print(f"Similarity between \n{files[i]} and {files[j]}: {similarity_percentage}%.")


# Example usage
directory_path = 'text/'  # Replace with the actual path to your directory
check_plagiarism(directory_path)
