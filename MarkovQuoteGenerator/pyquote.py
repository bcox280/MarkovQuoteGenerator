import sys


def create_t():
    print("")


def create_e():
    print("")


def main(args=None):
    """The main routine."""
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

        # Other method of populating

        # for words in line_words:
        #     if len(words) > 0:
        #         outQ.writelines(words[1].strip() + '\n')
        #         outA.writelines(words[0].strip() + '\n')


if __name__ == "__main__":
    main()
