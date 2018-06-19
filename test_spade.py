try:
    from spade.spade import *
except:
    from Spade.spade.spade import *


def test_calculate_support():
    words = ["rat", "mat"]
    assert gps_calculate_support(table_of_words=words, sequence="at") == 2


def test_get_unique_letters():
    words = ["abba", "ccd", "abc"]
    assert get_unique_supported_letters(word_database=words, min_support=2) == {"a", "b", "c"}


def test_init_poslist():
    words = ["abba", "ccd", "abc"]
    unique_letters = {"a", "b", "c"}
    answer = {'c': {0: [], 1: [0, 1], 2: [2]}, 'b': {0: [1, 2], 1: [], 2: [1]}, 'a': {0: [0, 3], 1: [], 2: [0]}}
    assert init_initial_poslist(unique_letters=unique_letters, word_database=words) == answer
