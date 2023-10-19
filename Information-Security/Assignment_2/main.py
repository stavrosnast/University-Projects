from nltk.book import *
from math import *
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk.tokenize
import nltk
import numpy as num
import pandas as pd
nltk.download('wordnet')

# QUESTION 1: Tokenize and create one-hot vectors for two sentences.
# Tokenize the first sentence using split and NLTK's word_tokenize.
sentence1 = "Thomas Jefferson began building Monticello at the age of 26."
sentence1.split()
a = str.split(sentence1)
print("Tokenized sentence1 with nltk: ", nltk.word_tokenize(sentence1)

# Tokenize the second sentence using split and NLTK's word_tokenize.
sentence2 = "There weren't 69 people indicted and 48 people—many of them top Nixon administration officials—convicted."
sentence2.split()
b = str.split(sentence2)
print("Tokenized sentence2 with nltk: ", nltk.word_tokenize(sentence2)

# Create one-hot vectors for both token sequences.
token_sequence = str.split(sentence1) 
vocab = sorted(set(token_sequence)) 
', '.join(vocab)
num_tokens = len(token_sequence)
vocab_size = len(vocab) 
onehot_vectors = num.zeros((num_tokens, vocab_size), int)
for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1
' '.join(vocab)
onehot_vectors
c1 = pd.DataFrame(onehot_vectors, columns=vocab)

token_sequence = str.split(sentence2)
vocab = sorted set(token_sequence)
', '.join(vocab)
num_tokens = len(token_sequence)
vocab_size = len(vocab)
onehot_vectors = num.zeros((num_tokens, vocab_size), int)
for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1
' '.join(vocab)
onehot_vectors
c2 = pd.DataFrame(onehot_vectors, columns=vocab)

# QUESTION 3: Create one-hot vectors for text4 and text7 with the first 50 tokens.
tokens3 = text4[:50]
import numpy as np
vocab = sorted(set(tokens3))
', '.join(vocab)
num_tokens = len(tokens3)
vocab_size = len(vocab)
onehot_vectors = np.zeros((num_tokens, vocab_size), int)
for i, word in enumerate(tokens3):
    onehot_vectors[i, vocab.index(word)] = 1
' '.join(vocab)
onehot_vectors
d = pd.DataFrame(onehot_vectors, columns=vocab)

tokens4 = text7[:50]
import numpy as np
vocab = sorted(set(tokens4))
', '.join(vocab)
num_tokens = len(tokens4)
vocab_size = len(vocab)
onehot_vectors = np.zeros((num_tokens, vocab_size), int)
for i, word in enumerate(tokens4):
    onehot_vectors[i, vocab.index(word)] = 1
' '.join(vocab)
onehot_vectors
e = pd.DataFrame(onehot_vectors, columns=vocab)

# QUESTION 4: Define a function to remove stopwords and create a positional index.
# Define the function to remove stopwords from tokens.
def stopwords(tokens):
    import string
    cleaned_tokens = []
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('english')
    for token in tokens:
        if token not in string.punctuation:
            cleaned_tokens.append(token)
    for token in tokens:
        if token not in stopwords:
            cleaned_tokens.append(token)
    return cleaned_tokens

# Define the function to create a positional index.
def positional_index(text):
    pos_index = {}
    text = [word.lower() for word in text]
    cleared_tokens = stopwords(text)
    dist = FreqDist(cleared_tokens).most_common(3)
    for key, n_appears in dist:
        pos_index[key] = [n_appears, []]
    for i, token in enumerate(text):
        for key in pos_index:
            if key == token:
                pos_index[key][1].append(i)
    return pos_index

f = positional_index(tokens3)
g = positional_index(tokens4)

# QUESTION 5, 6: Calculate cosine similarity between two text sequences.
# Define a function to calculate cosine similarity.
def cos_sin(text1, text2):
    stopwords = nltk.corpus.stopwords.words('english')
    l1 = []
    l2 = []
    text1S = {w for w in text1 if w not in stopwords}
    text2S = {w for w in text2 if w not in stopwords}
    rvector = text1S.union(text2S)
    for w in rvector:
        if w in text1S:
            l1.append(1)
        else:
            l1.append(0) 
        if w in text2S:
            l2.append(1) 
        else:
            l2.append(0) 
    c = 0
    for i in range(len(rvector): 
        c += l1[i] * l2[i] 
    return "{:.2%}".format(c / float((sum(l1) * sum(l2)) ** 0.5))

h = cos_sin(tokens3, tokens4)
i = cos_sin(text4, text7)
