from nltk.book import *
from math import *
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk.tokenize
import nltk
import string

# QUESTION 1A: Calculate vocabulary richness and word occurrences in text6 and text5.
# The richness function calculates the vocabulary richness with two decimal places.
def richness(word):
    print("Vocabulary Richness of", word, ":", "{:.2f}".format(len(word) / len(set(word)))
richness(text6)
print("Percentage of the word LAUNCELOT:", "{:.2%}".format(100 * text6.count("LAUNCELOT") / len(text6)))
print("Occurrences:", text6.count("LAUNCELOT"))
richness(text5)
print("Percentage of the words OMG, omg, and lol:", "{:.2%}".format(100 * text5.count("omg" or "OMG" or "lol") / len(text5)))
print("Occurrences:", text5.count("omg" or "OMG" or "lol"))

# QUESTION 1B: Calculate the percentages of specific words in text5 and text6.
x1 = (text5.count("and" or "weather" or "blacksmith") / len(text5)) * 100
x2 = (text6.count("know" or "and" or "weather") / len(text6)) * 100
x3 = (text5.count("weather") / len(text5)) * 100
x4 = (text6.count("and") / len(text5)) * 100

# QUESTION 3: Perform a frequency distribution analysis on text6.
fdist1 = FreqDist(text6)
fdist1
fdist1.most_common(50)
fdist1.plot(50)

# QUESTION 5: Tokenize and apply stemming and lemmatization to text2.
tokens1 = []
for x in range(200):
    tokens1.append(text2[x])

porter = PorterStemmer()
print("Porter: ", [porter.stem(t) for t in tokens1])
wnl = nltk.WordNetLemmatizer()
print("Lemmatizer:", [wnl.lemmatize(t) for t in tokens1])

# QUESTION 6: Tokenize a sentence using split and NLTK's word_tokenize.
sentence = "There weren't 69 people indicted and 48 people—many of them top Nixon administration officials—convicted."
print("Split:", sentence.split())
print("NLTK:", nltk.word_tokenize(sentence))

# QUESTION 7: Download and examine stopwords in English and Greek.
nltk.download('stopwords')
stopwordsenglish = nltk.corpus.stopwords.words('english')
stopwords_greek = nltk.corpus.stopwords.words('greek')

print("[Total in] English:", len(stopwordsenglish))
print("[Total in] Greek:", len(stopwords_greek))

# QUESTION 8: Remove stopwords from text2[:200] using the stopwords function.
tokens2 = text2[:200]
stopwords(tokens2)

# QUESTION 9: Plot frequency distributions with and without stopwords.
tokens2 = text2[:200]
FreqDist(tokens2).plot(50)
FreqDist(stopwords(tokens2)).plot(50)
