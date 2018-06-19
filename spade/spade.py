# def GSP(table_of_words, chars, min_support):
#     pass

def gps_calculate_support(table_of_words, sequence):
    """used for spade just for right now"""

    support = 0
    for word in table_of_words:
        if sequence in word:
            support += 1
    return support


# def gsp_extend_prefix_tree(array_of_bottom_nodes):
#     pass



def spade(current_sequence_position_tuples, min_support, previous_sequence_position_tuples, k_or_depth):
    pass


def spade_intersect(poslist_of_sequence_to_be_extended, poslist_of_sequence_to_be_used_for_extension):
    """
    Poslists are arrays of tuples related to a given sequence.
    They are of the form... word: [numbers]. Where word is a
    word in the database and [numbers] lists possible placements of the related sequence.

    This function takes two poslists (a,b) and outputs a poslist for sequence_a + sequence_b[k].

    :param poslist_of_sequence_to_be_extended:
    :param poslist_of_sequence_to_be_used_for_extension:
    :return: poslist_of_extended_sequence
    """

    pass


# tree implementation
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def main():
    start_tuple = (None, [])  # not finished
    start_node = Node(start_tuple)
    spade(start_node, 3, [], 0)


"""
Finds the unique letters that satisfy the min sup requirement
"""


def get_unique_supported_letters(word_database, min_support):
    unique_letters = set()
    unique_supported_letters = set()
    for word in word_database:
        for char in word:
            unique_letters.add(char)

    for char in unique_letters:
        support = 0
        for word in word_database:
            if char in word:
                support += 1
        if support >= min_support:
            unique_supported_letters.add(char)
    return unique_supported_letters


def init_initial_poslist(unique_letters, word_database):
    """

    :array[chars] unique_letters: all letters that have min support
    :array[words] word_database: all the sample words
    :return: initial poslist. For each unique min supported letter it lists the position of that letter in each sample word
    """
    poslist = {}
    for char in unique_letters:
        poslist[char] = {}
        for word_index, word in enumerate(word_database):
            poslist[char][word_index] = []

    for word_index, word in enumerate(word_database):
        for char_index, letter in enumerate(word):
            if letter in unique_letters:
                poslist[letter][word_index].append(char_index)
    return poslist
#