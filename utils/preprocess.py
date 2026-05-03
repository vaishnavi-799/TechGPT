import nltk
import string
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def preprocess(text):

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    return " ".join(tokens)
