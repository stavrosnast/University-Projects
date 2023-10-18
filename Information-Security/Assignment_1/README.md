# INFORMATION RETRIEVAL LAB - EXERCISE 1

## Introduction
This Python code provides examples of various natural language processing (NLP) tasks using the Natural Language Toolkit (NLTK) library. The code includes vocabulary richness calculation, word occurrences analysis, percentage calculations, frequency distribution analysis, tokenization, stemming, lemmatization, stopwords handling, and frequency distribution plotting. Each section of the code corresponds to a specific question or task.

## Prerequisites
Before running this code, ensure that you have the following Python libraries installed:

- NLTK
- NumPy (for specific sections)
- Matplotlib (for specific sections)

You can install these libraries using pip. Additionally, download the NLTK stopwords dataset by using `nltk.download('stopwords')`.

## Code Description
Here is a breakdown of the code sections:

### Question 1A: Vocabulary Richness and Word Occurrences
This section calculates the vocabulary richness and word occurrences in `text6` and `text5`. The `richness` function calculates vocabulary richness with two decimal places. Word occurrences and percentages for specific words are also analyzed.

### Question 1B: Percentage Calculations
This part calculates the percentages of specific words in `text5` and `text6`. It demonstrates how to analyze word frequencies and calculate percentages.

### Question 3: Frequency Distribution Analysis
This section performs a frequency distribution analysis on `text6`. It shows how to use NLTK to analyze word frequencies and plot the top 50 words in a text.

### Question 5: Tokenization and Text Processing
In this part, text2 is tokenized and then subjected to both stemming and lemmatization. The code demonstrates the use of NLTK's text processing tools for text normalization.

### Question 6: Tokenization of a Sentence
A sentence is tokenized using Python's `split` method and NLTK's `word_tokenize`. This section illustrates the tokenization process.

### Question 7: Stopwords Handling
Stopwords in both English and Greek are downloaded and examined. The code provides insights into working with stopwords in different languages.

### Question 8: Removing Stopwords
Stopwords are removed from a portion of `text2` using the `stopwords` function defined earlier. This showcases the removal of common stopwords from text data.

### Question 9: Frequency Distribution Plotting
Frequency distributions are plotted for the original token sequence and the sequence with stopwords removed. This section visually demonstrates the impact of stopwords on word frequency distribution.

## Usage
To use this code:

1. Ensure you have the required libraries installed.
2. Download the NLTK stopwords dataset.
3. Run the code in your preferred Python environment.

You can customize the input texts, specific words of interest, or text selections to explore different NLP scenarios. The code provides a foundation for common NLP tasks and data analysis.

## Conclusion
This code serves as a practical example of how to perform various NLP tasks using NLTK. It covers vocabulary richness, word occurrences, percentage calculations, frequency distribution analysis, tokenization, text processing, and stopwords handling. You can expand upon this code to address more complex NLP challenges and conduct in-depth text analysis.


## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of this license.
