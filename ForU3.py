import re

def word_processing():
    #Enter text from the keyboard
    text = input("Enter the text: ")

    #We break the text into words and remove punctuation marks
    words = re.findall(r'\b\w+\b', text)

    #We find the most common word
    most_common_word = max(set(words), key = words.count)

    #Finding the longest word
    longest_word = max(words, key = len)

    #We output the results
    print("The most common word: " + most_common_word)
    print("The longest word: " + longest_word)

if __name__ == "__main__":
    word_processing()