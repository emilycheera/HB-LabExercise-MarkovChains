"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    file_contents = open(file_path).read()

    return file_contents


def make_chains(text_string):
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

    bigrams = []

    for i in range(len(words)-1):
        bigrams.append((words[i], words[i+1]))

    bigrams = list(set(bigrams))

    for bigram in bigrams:

        for i in range(len(words)-2):

            if "".join(bigram) == (words[i] + words[i+1]):

                if bigram not in chains:
                    chains[bigram] = [words[i+2]]

                else:
                    chains[bigram].append(words[i+2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    starting_bigram = choice(list(chains.keys()))
    words.extend(starting_bigram)
    starting_value = choice(chains[starting_bigram])
    words.append(starting_value)

    new_key = (starting_bigram[1], starting_value)

    while True:
        if new_key in chains:
            random_value = choice(chains[new_key])
            words.append(random_value)
            new_key = (new_key[1], random_value)
        else:
            break

    # print(words)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
