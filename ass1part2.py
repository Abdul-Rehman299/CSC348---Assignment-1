# 2.2
def frequency_analysis(input_string):
    letter_frequency = {}

    symbols = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

    # Uppercase all the letters
    input_string = input_string.upper()

    for char in symbols:
        # Counts the occurrences of the character in the input string
        count = input_string.count(char)

        # Stores the frequency in the dictionary
        letter_frequency[char] = count

    # Sort the keys in the dictionary by alphabetical order (I didn't know if it was required, but i did anyways)
    sorted_frequency = dict(sorted(letter_frequency.items()))

    return sorted_frequency

# Usage:
input_string = "Hello, World!"
result = frequency_analysis(input_string)
print(result)


# 2.3
# Set frequencies
set_1 = {'A': 0.012, 'B': 0.003, 'C': 0.01, 'D': 0.1, 'E': 0.02, 'F': 0.001}
set_2 = {'A': 0.001, 'B': 0.012, 'C': 0.003, 'D': 0.01, 'E': 0.1, 'F': 0.02}
set_3 = {'A': 0.1, 'B': 0.02, 'C': 0.001, 'D': 0.012, 'E': 0.003, 'F': 0.01}

def cross_correlation(set_x, set_y):
    correlation = sum(set_x[val] * set_y[val] for val in set_x)
    return correlation

correlation_1with2 = cross_correlation(set_1, set_2)
correlation_1with3 = cross_correlation(set_1, set_3)

print("Cross-correlation between Set 1 and Set 2:", correlation_1with2)
print("Cross-correlation between Set 1 and Set 3:", correlation_1with3)


# 2.4
def frequency_analysis(input_string):
    # Initialize an empty dictionary to store frequencies
    letter_frequency = {}

    # Define the set of valid characters (uppercase letters and space)
    valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

    # Convert the input string to uppercase for case-insensitivity
    input_string = input_string.upper()

    # Loop through each valid character
    for char in valid_characters:
        # Count the occurrences of the character in the input string
        count = input_string.count(char)

        # Store the frequency in the dictionary
        letter_frequency[char] = count

    # Sort the dictionary by keys (letters) in alphabetical order
    sorted_frequency = dict(sorted(letter_frequency.items()))

    return sorted_frequency

def cross_correlation(set_x, set_y):
    correlation = sum(set_x[val] * set_y[val] for val in set_x)
    return correlation

def get_caesar_shift(enc_message, expected_dist):
    # Function to calculate the cross-correlation between two sets of values
    def cross_correlation(set_x, set_y):
        correlation = sum(set_x[val] * set_y[val] for val in set_x)
        return correlation

    # Function to calculate letter frequencies in a given string
    def frequency_analysis(input_string):
        # Initialize an empty dictionary to store frequencies
        letter_frequency = {}

        # Define the set of valid characters (uppercase letters and space)
        valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

        # Convert the input string to uppercase for case-insensitivity
        input_string = input_string.upper()

        # Loop through each valid character
        for char in valid_characters:
            # Count the occurrences of the character in the input string
            count = input_string.count(char)

            # Store the frequency in the dictionary
            letter_frequency[char] = count

        # Sort the dictionary by keys (letters) in alphabetical order
        sorted_frequency = dict(sorted(letter_frequency.items()))

        return sorted_frequency

    # Calculate the letter frequency of the encrypted message
    enc_freq = frequency_analysis(enc_message)

    # Calculate the cross-correlation for each possible shift
    shifts = range(27)
    correlations = {}

    for shift in shifts:
        # Shift the expected distribution
        shifted_dist = {}
        for char, freq in expected_dist.items():
            if char != ' ':
                index = (ord(char) - ord('A') + shift) % 26
                new_char = chr(index + ord('A'))
            else:
                new_char = ' '
            shifted_dist[new_char] = freq

        # Calculate cross-correlation with the shifted distribution
        correlation = cross_correlation(enc_freq, shifted_dist)
        correlations[shift] = correlation

    # Find the shift with the maximum cross-correlation
    likely_shift = max(correlations, key=correlations.get)

    return likely_shift

# Example usage:
enc_message = "Cqn arpqcb xo nenah vjw jan mrvrwrbqnm fqnw cqn arpqcb xo xwn vjw jan cqanjcnwnm"
expected_dist = {' ': 0.1828846265, 'E': 0.1026665037, 'T': 0.0751699827, 'A': 0.0653216702, 'O': 0.0615957725,
                 'N': 0.0571201113, 'I': 0.0566844326, 'S': 0.0531700534, 'R': 0.0498790855, 'H': 0.0497856396,
                 'L': 0.0331754796, 'D': 0.032829231, 'U': 0.0227579536, 'C': 0.0223367596, 'M': 0.0202656783,
                 'F': 0.0198306716, 'W': 0.0170389377, 'G': 0.0162490441, 'P': 0.0150432428, 'Y': 0.0142766662,
                 'B': 0.0125888074, 'V': 0.0079611644, 'K': 0.0056096272, 'X': 0.0014092016, 'J': 0.0009752181,
                 'Q': 0.000836755, 'Z': 0.0005128469}

shift = get_caesar_shift(enc_message, expected_dist)
print("Likely Caesar shift:", shift)

# 2.5 
 # I tried really really hard... but I was not able to make a completely successful Vigenere keywrod producer without faults or using ord() and chr(), which I think goes against the symbol set we are using. :(