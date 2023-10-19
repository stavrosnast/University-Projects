# INFORMATION RETRIEVAL LAB - EXERCISE 3 [Levenshtein Distance Calculator]

This Python script calculates the Levenshtein distance between two input strings, demonstrating a simple implementation of the Levenshtein algorithm. The Levenshtein distance measures the number of single-character edits required to change one string into another. 

## Usage

To calculate the Levenshtein distance between strings, simply call the `iterative_levenshtein` function with your two strings as arguments. The function returns the Levenshtein distance as an integer.

For example:

```python
distance = iterative_levenshtein("kitten", "sitting")
print("Levenshtein distance:", distance)
```

## How It Works

The code initializes a Levenshtein matrix, where each cell represents the cost of converting one string into another. It follows these steps:

1. Initialize the dimensions of the Levenshtein matrix based on the lengths of the input strings.
2. Fill in the matrix by initializing source and target prefixes.
3. Calculate the Levenshtein distance by comparing characters in both strings.
4. Determine the cost for insertion, deletion, and substitution.
5. Update the matrix cells with the minimum cost among the three possible operations.
6. The final value in the last cell of the matrix represents the Levenshtein distance.

## Examples

The code provides examples for calculating the Levenshtein distance between pairs of English and Greek words. You can replace the sample word pairs to calculate the Levenshtein distance for your specific use case.

## Credits

- Original author: rahulsinghal1904
- Code inspiration source: [GeeksforGeeks - Correcting Words Using NLTK in Python](https://www.geeksforgeeks.org/correcting-words-using-nltk-in-python/)
- Utility used for misspelled text: [Online-Utility - Misspellizer](https://www.online-utility.org/text/misspellizer.jsp)

## Dependencies

The script uses the Natural Language Toolkit (NLTK) library for Levenshtein distance calculation. Make sure to install NLTK and its dependencies before running the code.

```bash
pip install nltk
```

Additionally, it uses the NLTK corpus "words" for comparing incorrect words. You can download it using:

```python
nltk.download('words')
```

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of this license.
