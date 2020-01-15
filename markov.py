"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    file_path = sys.argv[1]

    file_contents = open(file_path).read()

    return file_contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    n_grams = []

    for i in range(len(words)-(n-1)):
        each_n_gram = []
        for j in range(n):
            each_n_gram.append(words[i + j])
        n_grams.append(tuple(each_n_gram))

    n_grams = list(set(n_grams))

    for n_gram in n_grams:

        for i in range(len(words)-n):

            test_string = ''
            for j in range(n):
                test_string += words[i + j]

                if "".join(n_gram) == test_string:

                    if n_gram not in chains:
                        chains[n_gram] = [words[i+n]]

                    else:
                        chains[n_gram].append(words[i+n])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    starting_n_gram = choice(list(chains.keys()))

    n = len(starting_n_gram)
    
    while starting_n_gram[0][0].isupper() == False:
        starting_n_gram = choice(list(chains.keys()))

    words.extend(starting_n_gram)
    starting_value = choice(chains[starting_n_gram])
    words.append(starting_value)

    new_key = []
    for i in range(1, n):
        new_key.append(starting_n_gram[i])
    new_key.append(starting_value)
    new_key = tuple(new_key)

    while True:
        if new_key in chains:
            random_value = choice(chains[new_key])
            words.append(random_value)
            temp_new_key = []
            for i in range(1, n):
                temp_new_key.append(new_key[i])
            temp_new_key.append(random_value)
            new_key = tuple(temp_new_key)
        else:
            break

    # print(words)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains)

print(random_text)
