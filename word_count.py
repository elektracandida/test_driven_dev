def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    return map(len, s.split()) 

def get_character(s, c):
    """ 
    Returns the number of times that character c appears
    in sentence s.
    """ 
    return s.count(c)    

def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]

def test_get_character():
    text = "My name is Bond"
    assert get_character(text, 'y') == 1

test_get_word_lengths()
test_get_character()
