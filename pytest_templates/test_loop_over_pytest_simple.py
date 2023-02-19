"""
Looping over pytest tests.
"""

import pytest


def simple_pig_latin(word: str) -> str:
    """Simple function to translate a single word into the
    pig latin equivalent. Move the first letter to the end
    and add 'ay' on to that. For example, 'hello' becomes
    'ellohay'

    Args:
        word: a single word.
    returns:
        The equivalent word in pig latin.
    """
    piglatin_word = word[1:] + word[0] + "ay"
    return piglatin_word


print(simple_pig_latin("howdy"))

# @pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize(
    "test_input,expected",
    [("howdy", "owdyhay"), ("hello", "ellohay"), (" ahoy", "hoyaay")],
)
def test_simple_pig_latin(test_input, expected):
    assert simple_pig_latin(test_input) == expected
