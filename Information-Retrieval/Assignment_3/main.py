def iterative_levenshtein(s, t):
    # Initialize the dimensions of the Levenshtein matrix
    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    # Fill in the matrix to calculate the Levenshtein distance
    # Initialize the source prefixes
    for i in range(1, rows):
        dist[i][0] = i

    # Initialize the target prefixes
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0  # No cost for matching characters
            else:
                cost = 1  # Cost of 1 for substitution

            # Calculate minimum cost among deletion, insertion, and substitution
            dist[row][col] = min(dist[row - 1][col] + 1,  # Deletion
                                 dist[row][col - 1] + 1,  # Insertion
                                 dist[row - 1][col - 1] + cost)  # Substitution

    return dist[rows - 1][cols - 1]
print("English Words:")
# ENGLISH WORDS
print(iterative_levenshtein("aboutt", "about"))
print(iterative_levenshtein("lal", "all"))
print(iterative_levenshtein("laso", "also"))
print(iterative_levenshtein("nda", "and"))
print(iterative_levenshtein("bbecause", "because"))
print(iterative_levenshtein("nbut", "but"))
print(iterative_levenshtein("cann", "can"))
print(iterative_levenshtein("cohme", "come"))
print(iterative_levenshtein("ciould", "could"))
print(iterative_levenshtein("dayy", "day"))
print(iterative_levenshtein("evden", "even"))
print(iterative_levenshtein("fjind", "find"))
print(iterative_levenshtein("foirst", "first"))
print(iterative_levenshtein("foor", "for"))
print(iterative_levenshtein("frmo", "from"))
print(iterative_levenshtein("geet", "get"))
print(iterative_levenshtein("givve", "give"))
print(iterative_levenshtein("habve", "have"))
print(iterative_levenshtein("theri", "her"))
print(iterative_levenshtein("toher", "here"))
print(iterative_levenshtein("hiim", "him"))
print(iterative_levenshtein("whisch", "his"))
print(iterative_levenshtein("thowse", "how"))
print(iterative_levenshtein("ointo", "into"))
print(iterative_levenshtein("itts", "its"))
print(iterative_levenshtein("juwst", "just"))
print(iterative_levenshtein("knoow", "know"))
print(iterative_levenshtein("luike", "like"))
print(iterative_levenshtein("olok", "look"))
print(iterative_levenshtein("mmany", "make"))
print(iterative_levenshtein("maan", "man"))

print("Greek Words:")
# GREEK WORDS
print(iterative_levenshtein("αιβδομ΄΄αδα", "εβδομάδα"))
print(iterative_levenshtein("τέος", "έτος"))
print(iterative_levenshtein("σιμαιρα", "σήμερα"))
print(iterative_levenshtein("ριοαύ", "αύριο"))
print(iterative_levenshtein("χθαις", "χθες"))
print(iterative_levenshtein("οιμαιρολώγιο", "ημερολόγιο"))
print(iterative_levenshtein("δαιτελρπτοτ", "δευτερόλεπτο"))
print(iterative_levenshtein("ορα", "ώρα"))
print(iterative_levenshtein("ληπτο", "λεπτό"))
print(iterative_levenshtein("λοιρο", "ρολόι"))
print(iterative_levenshtein("μπορο", "μπορώ"))
print(iterative_levenshtein("χροισαμοποιεω", "χρησιμοποιώ"))
print(iterative_levenshtein("νικανο", "κάνω"))
print(iterative_levenshtein("πθυγαίονω", "πηγαίνω"))
print(iterative_levenshtein("αιρσχχωμα", "έρχομαι"))
print(iterative_levenshtein("φτοαχψμ", "φτιάχνω"))
print(iterative_levenshtein("γλταψωωα", "γελάω"))
print(iterative_levenshtein("βλαδφςπ", "βλέπω"))
print(iterative_levenshtein("όόμορφφός", "όμορφος"))
print(iterative_levenshtein("κδαλφςασπερα", "Καλησπέρα"))


"""
# ORIGINAL AUTHOR::: rahulsinghal1904
# URL:: <https://www.geeksforgeeks.org/correcting-words-using-nltk-in-python/>
# UTILITY USED FOR MISSPELLED TEXT URL:: <https://www.online-utility.org/text/misspellizer.jsp>
"""

# importing the nltk suite
import nltk
# importing edit distance
from nltk.metrics.distance  import edit_distance
# Downloading and importing package 'words'
nltk.download('words')
from nltk.corpus import words
correct_words = words.words()

# list of incorrect spellings that need to be corrected with 2 levels of Mispell level
incorrect_words_level_1 = ['happpy', 'azmaing', 'intelliengt', 'Yuo', 'serivcse', 'wyas', 'maange', 'yuro', 'priavcy', 'exampel',  'cna ', 'sgin', 'fro', 'Gooleg', 'Acucont', 'watn',
                           'craeet', 'manaeg', 'contnet ', 'emiasl ', 'adn', 'phtoos',  'mroe', 'serahc', 'reuslts', 'Adn', 'yuo', 'cna', 'Gogole', 'wenh', 'sigend', 'otu', 'creaintg',
                           'accoutn', 'saerching', 'Gooegl', 'watchgin', 'chooes', 'wbe', 'pirvtaely', 'uisng', 'Chrmoe', 'Inocgniot', 'arcoss', 'oru', 'sevriecs', 'ajdust', 'yuor', 'privayc',
                           'stetings', 'whta', 'clolect']

incorrect_words_level_0 = ['Throguh', 'thsi', 'lenared', 'basisc', 'tohugh', 'teh', 'lirbary', 'vats', 'colud', 'nto',
                           'cvoer', 'artciel', 'woudl', 'wolud', 'porjcet', 'taht', 'unedrstand', 'gievn', 'tmei', 'adn', 'effrto']
# loop for finding correct spellings  based on edit distance and printing the correct words, level 0
for word in incorrect_words_level_0:
    temp = [(edit_distance(word, w), w)
            for w in correct_words if w[0] == word[0]]
    print("Level 0: ",sorted(temp, key=lambda val: val[0])[0][1])
# loop for finding correct spellings  based on edit distance and printing the correct words, level 1
for word in incorrect_words_level_1:
    temp = [(edit_distance(word, w), w)
            for w in correct_words if w[0] == word[0]]
    print("Level 1: ",sorted(temp, key=lambda val: val[0])[0][1])