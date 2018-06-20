try:
    from spade.spade import *
except:
    from Spade.spade.spade import *


def test_get_unique_letters():
    words = ["abba", "ccd", "abc"]
    assert get_unique_supported_letters(word_database=words, min_support=2) == {"a", "b", "c"}


def test_init_poslist():
    words = ["abba", "ccd", "abc"]
    assert init_poslist(input_letter="a", word_database=words) == {0: [0, 3], 1: [], 2: [0]}


def test_init_spade__init_poslists():
    words = ["abba", "ccd", "abc"]
    current_generation = init_spade(word_database=words, min_support=2)
    for node in current_generation:
        if node.sequence == "a":
            assert node.poslist == {0: [0, 3], 1: [], 2: [0]}
        elif node.sequence == "b":
            assert node.poslist == {0: [1, 2], 1: [], 2: [1]}
        else:
            assert node.poslist == {0: [], 1: [0, 1], 2: [2]}


def test_init_spade_get_parent():
    words = ["abba", "ccd", "abc"]
    current_generation = init_spade(word_database=words, min_support=2)
    assert (current_generation[0].parent == current_generation[1].parent) and (
            current_generation[2].parent == current_generation[1].parent)


def test_intersection():
    # (self, sequence, poslist)
    parent_of_a_g = Node("asdasd", {})

    node_a_poslist = {0: [1, 3, 4], 1: [2, 4], 2: [1, 2]}
    node_a = Node("a", node_a_poslist)
    parent_of_a_g.add_child(node_a)

    node_g_poslist = {0: [2, 5], 1: [1, 5], 2: [0, 3]}
    node_g = Node("g", node_g_poslist)

    parent_of_a_g.add_child(node_g)
    output = intersection(node_a, node_g)

    assert output == {0: [2, 5], 1: [5], 2: [3]}

def test_extend_sequence():
    node_a_poslist = {0: [1, 3, 4], 1: [2, 4], 2: [1, 2]}
    node_a = Node("a", node_a_poslist)

    node_g_poslist = {0: [2, 5], 1: [1, 5], 2: [0, 3]}
    node_g = Node("g", node_g_poslist)


    extend_sequence()


def calculate_support():
    poslist = {}
    poslist[1] = [1, 2, 3]
    poslist[2] = [1, 3]
    poslist[3] = [2]
    answer = 3
    assert calculate_support(poslist_of_substring=poslist) == answer
