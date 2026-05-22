""" 
This programme is used to detect plagiarism between two essays, check if the word input by the user is in both essays
and also count the frequency of words in both essays the essays.

"""
import string 
"""
For us to be able to use python's inbuilt string module.
"""

def reading_file(filename):
    """
    Reading and opening the essay files.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Sorry, file {filename} not found...")
        return ""

def converting_text(text):
    """
    Converting the text from the essay files into split word.
    """
    #converting all the text to lower case
    text = text.lower()
    #Removing all the panctuation marks
    trans_table = str.maketrans('', '', string.punctuation)
    text = text.translate(trans_table)

    #Now that we have have removed punctiontion marks and capital letters, we split the words.
    words = text.split()

    return words

def counting_words(words):
    """
    Now that we have prepared the words, this function is going to be used to 
    count the frequency of the words using a dictionary.
    """
    word_dict = {}

    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

def finding_common_words(section_1, section_2):
    """
    Finding words that appear in both essays.
    """
    common = set(section_1.keys()) & set(section_2.keys())

    print("    COMMON WORDS    ")

    for word in sorted(common):
        print(f"\n{word:<15} Essay_1: {section_1[word]:<3} Essay_2 {section_2[word]}")

    return common


def search_word(word, section_1, section_2):
    """
    Searches for a specific word in both essays, 
    Returns true if the word appears in both, otherwise returns false. 
    """
    word = word.lower()

    if word in section_1 and word in section_2:
        print(f"\n {word} found: ")
        print(f"Number of times in Essay_1:  {section_1[word]}")
        print(f"Number of times in Esaay_2:  {section_2[word]}")
        return True
    else:
        print(f"\n'{word}' not found in both essays.")
    return False


def calculate_plagiarism(words1, words2):
    """
    Calculates the percentage of plagiarism using the formula:
    intersection / union * 100
    """
    #converting the words into sets
    set_1 = set(words1)
    set_2 = set(words2)

    intersection = set_1 & set_2

    union = set_1 | set_2

    #calculating the percentage of plagiarism
    plagiarism_percentage = (len(intersection) / len(union)) * 100

    print("\nPLAGIARISM ANALYSIS")
    print("-" * 30)
    print(f"Common words: {len(intersection)}")
    print(f"Total unique words: {len(union)}")
    print(
        f"Plagiarism Percentage: "
        f"{plagiarism_percentage:.2f}%"
    )

    if plagiarism_percentage >= 50:
        print("PLAGIARISM DETECTED")
    else:
        print("NO PLAGIARISM DETECTED")

    return plagiarism_percentage


def main():
    """
    Main function of the program
    """
    #reading the essay files
    essay_1 = reading_file("essay1.txt")
    essay_2 = reading_file("essay2.txt")

    # converting text
    words1 = converting_text(essay_1)
    words2 = converting_text(essay_2)

    # counting words
    section_1 = counting_words(words1)
    section_2 = counting_words(words2)

    #finding common words
    common_words = finding_common_words(section_1, section_2)

    print(f"\nTotal Common Words: {len(common_words)}")

    # Search for a specific word                               
    search = input(
        "\nEnter a word to search in both essays: "
    ).strip()

    if search:
        search_word(search, section_1, section_2)  
    else:
        print("Invalid input.")

    # Calculate plagiarism percentage
    calculate_plagiarism(words1, words2)


if __name__ == "__main__":
    main()