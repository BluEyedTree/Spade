
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
node_a is to extend
node_b is extending node_a

'''

def intersection(node_a, node_b):
    # The first condition is that Noda_A and Node_B are from the same sequence
    assert (node_a.parent == node_b.parent), "Function was called with nodes of different parents"

    poslist_a_b = {}

    # The second condition
    # A letter from node_a must be before a letter in node_b
    for sequence in list(node_a.poslist.keys()):
        first_occurance_noda_a = node_a.poslist.get(sequence)[0]
        all_occurance_node_b = node_b.poslist.get(sequence)
        occurances_node_a_b = []
        # Ensure that node_b has the sequence
        if (all_occurance_node_b is not None):
            for occurance_node_b in all_occurance_node_b:
                if (occurance_node_b > first_occurance_noda_a):
                    occurances_node_a_b.append(occurance_node_b)
        # Ensure that condition two was satisfied, and occurances_node_a_b is not empty
        if (len(occurances_node_a_b) > 0):
            poslist_a_b[sequence] = occurances_node_a_b

    return poslist_a_b


def extend_sequence(node_a, node_b):
    # The first condition is that Noda_A and Node_B are from the same sequence
    assert (node_a.parent == node_b.parent), "Function was called with nodes of different parents"

    sequence_a_b = node_a.sequence + node_b.sequence[-1]

    return sequence_a_b



def spade(current_generation, min_support, history, k_or_depth):
    history[k_or_depth] = current_generation
    next_generation = []

    for node in current_generation:
        for sibling_node in node.parent.children:
            new_sequence = extend_sequence(node, sibling_node)
            new_poslist = intersection(node, sibling_node)
            if len(new_poslist) >= min_support:
                new_node = Node(sequence=new_sequence, poslist=new_poslist)
                node.add_child(new_node)
                next_generation.append(new_node)


    if len(next_generation) > 0:
        return spade(next_generation, min_support, history, k_or_depth+1)
    else:
        return history

def run_spade(word_database, min_support):
    init_generation = init_spade(word_database, min_support)
    results = spade(init_generation, min_support, history={}, k_or_depth=0)
    return results



def main():
    # TODO: replace with user input
    # word_database = ["abba", "ccd", "abc"]
    word_database = ["CAGAAGT",
                     "TGACAG",
                     "GAAGT"
                     ]


    min_support = 3

    results = run_spade(word_database, min_support)
    for layer_num in results:
        layer = results[layer_num]
        print()
        print("Layer: " + str(layer_num))
        print()
        for node in layer:
            print(node.sequence)


            for item in node.poslist:
                print("\t"+ str(item), end=' \t')

                print(node.poslist[item])






if __name__ == '__main__':
    main()
