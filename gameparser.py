# Game Parser File

# Need to make key words list!

# Functions Needed:
# Remove Punctuation
# Remove Whitespace
# Filter Keywords

import string

key_words = ['north', 'south', 'east', 'west', 'go', 'drop', 'take', 'use',
             'sword', 'keys', 'ore', 'gem', 'armour', 'trident', 'whiskey']
# ADD MORE LATER??

def remove_punctuation(text):

    # Used to remove all punctuation from a string (not including spaces)

    no_punctuation = ""

    for character in text:

        if not (character in string.punctuation):

            no_punctuation = no_punctuation + character

    return no_punctuation

def filter_words(words, key_words):

    # Filter Words so only words from keywords list are in list

    filtered_words = []

    for word in words:

        if word in key_words:
            filtered_words.append(word)

    return filtered_words

def normalise_input(user_input):

    # Removes all punctuation, converts to lower case, removes spaces
    # Also splits into string of words that are "important"

    no_punctuation = remove_punctuation(user_input)
    
    lower_case = no_punctuation.lower()

    no_whitespace = lower_case.strip()

    unfiltered_list = no_whitespace.split()

    filtered_list = filter_words(unfiltered_list, key_words)

    return filtered_list
