import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = "I love learning about Large Language Models!"
tokens = word_tokenize(text)

print(tokens)
