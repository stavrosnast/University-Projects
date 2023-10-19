# INFORMATION RETRIEVAL LAB - EXERCISE 2

## Introduction
This Python code is designed to demonstrate various natural language processing (NLP) tasks using the Natural Language Toolkit (NLTK) library. The code includes tokenization, one-hot vector creation, stopwords removal, positional indexing, and cosine similarity calculation. Each section of the code corresponds to a specific question or task.

## Prerequisites
Before running this code, you will need to ensure that you have the following Python libraries installed:

- NLTK
- NumPy
- Pandas

You can install these libraries using pip. Additionally, you need to download NLTK's wordnet dataset using `nltk.download('wordnet')`.

## Code Description
Here is a breakdown of the code sections:

### Question 1: Tokenization and One-Hot Vectors
In this section, two sentences are tokenized using both Python's built-in `split` and NLTK's `word_tokenize`. One-hot vectors are created for each token sequence. The code demonstrates the tokenization and vectorization process.

### Question 3: One-Hot Vectors for Text4 and Text7
Here, one-hot vectors are generated for the first 50 tokens from Text4 and Text7. This section showcases how to create one-hot vectors for specific sections of text.

### Question 4: Stopwords Removal and Positional Indexing
This part defines two functions. The first function, `stopwords`, removes stopwords and punctuation from a list of tokens. The second function, `positional_index`, creates a positional index for tokens by finding the positions of specific keywords. The code demonstrates how to clean text data and create a simple positional index.

### Question 5 and 6: Cosine Similarity Calculation
Two functions, `cos_sin`, are defined to calculate cosine similarity between two text sequences. Stopwords are removed, and a cosine similarity metric is calculated to determine how similar the texts are.

## Usage
To use this code:

1. Ensure you have the required libraries installed.
2. Download the NLTK wordnet dataset.
3. Run the code in your preferred Python environment.

You can modify the input sentences, text selections, and keywords to test different scenarios. The code provides a foundation for performing common NLP tasks.

## Conclusion
This code serves as an educational example of how to perform various NLP tasks using NLTK. It demonstrates tokenization, vectorization, stopwords removal, positional indexing, and cosine similarity calculation. You can build upon this code to tackle more complex NLP challenges.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of this license.
