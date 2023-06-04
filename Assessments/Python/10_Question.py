import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def count_pos(phrase):
    # Tokenize the phrase into words
    words = word_tokenize(phrase)

    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)

    # Initialize counts
    counts = {
        'verb': 0,
        'noun': 0,
        'pronoun': 0,
        'adjective': 0
    }

    # Count the occurrences of each part of speech
    for word, tag in tagged_words:
        if tag.startswith('VB'):
            counts['verb'] += 1
        elif tag.startswith('NN'):
            counts['noun'] += 1
        elif tag == 'PRP' or tag == 'PRP$':
            counts['pronoun'] += 1
        elif tag.startswith('JJ'):
            counts['adjective'] += 1

    return counts

# Test case 1: Count the parts of speech in a phrase
phrase1 = "The cat sat on the mat."
result1 = count_pos(phrase1)
print("Counts for test case 1:")
print(result1)

# Test case 2: Count the parts of speech in a paragraph
paragraph2 = "I went to the park and saw a beautiful flower. It was red and smelled amazing."
result2 = count_pos(paragraph2)
print("Counts for test case 2:")
print(result2)
