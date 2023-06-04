from collections import Counter

def is_valid_string(s):
    # Count the frequencies of characters in the string
    frequencies = Counter(s)

    # Check if all frequencies are the same
    if len(set(frequencies.values())) == 1:
        return "YES"

    # Check if removing one character makes all frequencies the same
    for char in frequencies:
        frequencies[char] -= 1
        updated_frequencies = list(frequencies.values())

        # Remove zeros from the list of frequencies
        updated_frequencies = [freq for freq in updated_frequencies if freq != 0]

        # Check if all remaining frequencies are the same
        if len(set(updated_frequencies)) == 1:
            return "YES"

        # Revert the decrement
        frequencies[char] += 1

    return "NO"

# Test case 1
s = "abc"
print(is_valid_string(s))  # Output: YES