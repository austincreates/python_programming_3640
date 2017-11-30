import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT') or line.startswith('**START OF THE PROJECT'):
            break
        # INSERT CODE BELOW
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT') or line.startswith('**START OF THE PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())
    #pass


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)
    #pass


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    freq = []
    for key, value in hist.items():
        temp = [value, key]
        freq.append(temp)
    freq.sort(reverse = True)    
    return freq
    #pass


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
         print(word, '\t', freq)
    #pass


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    dic2 = {}
    for key, value in d1.items():
        if key not in d2:
            dic2[key] = dic2.get(key, value)
    return dic2
            
    #pass


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    rando = []
    for key, value in hist.items():
        rando.extend([key] * value)
    return random.choice(rando)


def main():
    hist = process_file('Dracula.txt', skip_header=True)
    print (hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[0:20]:
         print(word, '\t', freq)

    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')
    


if __name__ == '__main__':
    main()