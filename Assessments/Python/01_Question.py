def find_highest_frequency_word_length(string):
    words = string.split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    max_frequency = max(frequency.values())
    highest_frequency_words = [word for word, freq in frequency.items() if freq == max_frequency]
    highest_frequency_word_length = len(max(highest_frequency_words, key=len))
    
    print("Highest Frequency Word: ", highest_frequency_words[0])
    print("Frequency: ", max_frequency)
    print("Highest Frequency Word Length: ", highest_frequency_word_length)
    

# Example input
# string = "write write write all the number from from from 1 to 100"
string = input("Enter String: ")
find_highest_frequency_word_length(string)
# Output: 5
