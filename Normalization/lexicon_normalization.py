
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()


word = "multiplying"
print("_lenna :",lem.lemmatize(word,"v"))

print("_stem :",stem.stem(word))