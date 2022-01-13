import string
from hash_table.hash_table import HashTable


def find_first_repeat(sample):
    # process sample string - lowercase, no punctuation, split into list
    sample = sample.lower()

    trans_table = str.maketrans('', '', string.punctuation)
    sample_no_punct = sample.translate(trans_table)

    sample_list = sample_no_punct.split()

    # search for repetitions using hash table
    ht = HashTable()

    for word in sample_list:
        if ht.contains(word):
            return word
        else:
            ht.add(word, word)

    # return default message if no repetition found
    return "No repeated strings found!"
