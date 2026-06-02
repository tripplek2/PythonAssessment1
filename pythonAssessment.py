import re

# Read the newx article from the txt file.
def read_article(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    
# Count number of times a specific word appears
def count_specific_word(text, search_word):
    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())