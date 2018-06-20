# def GSP(table_of_words, chars, min_support):
#     pass

# def gps_calculate_support(table_of_words, sequence):
#     """used for spade just for right now"""
#
#     support = 0
#     for word in table_of_words:
#         if sequence in word:
#             support += 1
#     return support


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
    def __init__(self, sequence, poslist):
        self.parent = None
        self.children = []
        self.sequence = sequence
        self.poslist = poslist

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self


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


def init_poslist(input_letter, word_database):
    poslist_letter = {}
    for word_index, word in enumerate(word_database):
        poslist_letter[word_index] = []
        for char_index, char in enumerate(word):
            if input_letter == char:
                poslist_letter[word_index].append(char_index)
    return poslist_letter


def init_spade(word_database, min_support):
    init_node = Node(sequence=None, poslist=None)
    unique_chars = get_unique_supported_letters(word_database, min_support)
    init_generation = []
    for char in unique_chars:
        new_node = Node(sequence=char, poslist=init_poslist(char, word_database))
        init_node.add_child(new_node)
        init_generation.append(new_node)
    return init_generation
'''
node_a is to extended
node_b is extending node_a

'''
def intersection(node_a, node_b):
    #The first condition is that Noda_A and Node_B are from the same sequence
    assert (node_a.parent == node_b.parent), "Function was called with nodes of different parents"

    poslist_a_b = {}

    #The second condition
    #A letter from node_to_be_extended must be before a letter in node_to_extend_with
    for sequence in  list(node_a.poslist.keys()):
        first_occurance_noda_a = node_a.poslist.get(sequence)[0]
        all_occurance_node_b = node_b.poslist.get(sequence)
        occurances_node_a_b = []
        #Ensure that node_b has the sequence
        if(all_occurance_node_b is not None):
            for occurance_node_b in all_occurance_node_b:
                if(occurance_node_b > first_occurance_noda_a):
                    occurances_node_a_b.append(occurance_node_b)
        #Ensure that condition two was satisfied, and occurances_node_a_b is not empty
        if(len(occurances_node_a_b) >0 ):
            poslist_a_b[sequence] = occurances_node_a_b

    return poslist_a_b


def extend_sequence(node_a, node_b):
    pass


'''
"""
Calculates the support of a given substring.
The support is the number of distinct sequences that the substring occurs. Or the length of the poslist.
Input:
A poslist of a substring

Example input:
{1:[1,2,3]}

Output:
Integer

Example output:
1
"""


def calculate_support(poslist_of_substring):
    return len(list(poslist_of_substring.keys()))
'''