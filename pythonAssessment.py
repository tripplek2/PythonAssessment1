import re

# Read the news article from the txt file.
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
    
    most_common = max(word_count, key=word_count.get)

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

# Count paragraphs
def count_paragraphs(text):
    if text.strip() == "":
        return 1
    
    paragraphs = text.split("\n\n")

    count = 0

    for paragraph in paragraphs:
        if paragraph.strip() != "":
            count += 1
    
    return count

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

# Main function
def main():

    article = read_article("news_article.txt")

    print("News article analyzer")

    search_word = "" 
    
    # While loop
    while search_word.strip() == "":
        search_word = input("Enter a word to search for: ")

    word_count = count_specific_word(article, search_word)
    common_word = identify_most_common_word(article)
    average_length = calculate_average_word_length(article)
    paragraph_count = count_paragraphs(article)
    sentence_count = count_sentences(article)

    print("\n---Results---")
    print(f"Occurences of '{search_word}':{word_count}")
    print(f"Most common word: {common_word}")
    print(f"Average word length: {average_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")
   
if __name__ == "__main__" :
    main()


