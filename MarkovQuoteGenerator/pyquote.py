import sys
import numpy as np
from itertools import islice
import random

transition = {}
prior = {}


def generate_next(current):
    """Generate the next word in the quote"""
    return generate_init(transition[current])


def generate_init(dictionary):
    """Generate the first word that'll be the 'seed' for the quote"""
    weighted = []
    for key in dictionary:
        for value in [key] * dictionary[key]:
            weighted.append(value)

    return random.choice(weighted)


def add_to_p(word):
    """Add to initialised prior vector of all starting words"""
    if word in prior:
        prior[word] = prior[word] + 1
    else:
        prior[word] = 1


def add_in(s, t):
    """Add corresponding words into a dictionary of dictionaries"""

    if s in transition:
        inner_dict = transition[s]
        if t in inner_dict:
            inner_dict[t] = inner_dict[t] + 1
        else:
            inner_dict[t] = 1
    else:
        transition[s] = {t: 1}


def create_t():
    """Create the transition object."""
    inf = open("../SourceText/quotes.txt", "r")
    lines = (text.split() for text in inf)

    for line in lines:
        first_word = line[0]
        add_to_p(first_word)
        for other_word in line[1:]:
            add_in(first_word, other_word)
            first_word = other_word

    quote = generate_init(prior)
    current_word = quote

    while True:
        current_word = generate_next(current_word)
        quote = quote + " " + current_word
        if current_word.endswith('.'):
            break

    print(quote)


def create_e():
    """Create the emissions matrix."""
    print("")


def generate(args=None):
    """Generate a quote as a sequence of words."""

    if args is None:
        args = sys.argv[1:]

    # Open the corpus and split on the delimiter, the tab character
    with open("../SourceText/author-quote.txt", "r") as inf, \
            open("../SourceText/quotes.txt", "w") as outQ, \
            open("../SourceText/authors.txt", "w") as outA:
        line_words = (line.split('\t') for line in inf)
        outA.writelines(words[0].strip() + '\n' for words in line_words if len(words) > 1)

        # Reopen as all lines were exhausted
        # This is somehow faster than writing inbetween 1 for loop and initialising each variable
        inf = open("../SourceText/author-quote.txt", "r")
        line_words = (line.split('\t') for line in inf)
        outQ.writelines(words[1].strip() + '\n' for words in line_words if len(words) > 1)

    create_t()


if __name__ == "__main__":
    generate()
