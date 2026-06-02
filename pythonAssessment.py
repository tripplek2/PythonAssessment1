import re

# Read the newx article from the txt file.
def read_article(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    
# Count number of times a specific word appears
def count_specific_word(text, search_word):
    words = re.findall(r"\b\w+\b", text.lower())
    return words.count(search_word.lower())

# Find the most common word
def identify_most_common_word(text):
    words = re.findall(r"\b\w+\b", text.lower())

    if len(words) == 0:
        return None
    
    word_count = {}

    # for loop
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    most_common = max(word_count, key=word.count.get)

    return most_common

# Calculate average word length
def calculate_average_word_length(text):

    if text.strip() == "":
        return 0
    
    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0
    
    total_letters = 0

    for word in words:
        total_letters += len(word)
    
    average = total_letters / len(words)

    return average

# Count sentences
def count_sentences(text):

    if text.strip() == "":
        return 1
    
    sentences = re.split(r"[.!?]+", text)

    count = 0

    for sentence in sentences:
        if sentence.strip() != "":
            count += 1
            return count

# Main

