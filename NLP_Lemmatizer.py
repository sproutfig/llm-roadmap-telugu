import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("running"))   # run
print(lemmatizer.lemmatize("studies"))   # study
