from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('stopwords')

text = "This is a simple example of stop word removal."
tokens = word_tokenize(text)

filtered = [word for word in tokens if word.lower() not in stopwords.words('english')]

print(filtered)
