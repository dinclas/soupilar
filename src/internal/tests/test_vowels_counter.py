import pytest
from ..vowels_counter import VowelsCounter


@pytest.fixture
def vowels():
    return "aeiou"


@pytest.fixture
def non_vowels(vowels):
    all_characters = [chr(r) for r in range(0, 256)]
    characters_without_lowercase_vowels = [r for r in all_characters if r not in vowels]
    characters_without_any_vowels = [
        r for r in characters_without_lowercase_vowels if r not in vowels.upper()
    ]
    return "".join(characters_without_any_vowels)


def test_count_all_vowels(vowels):
    result = VowelsCounter.count_vowels(vowels)
    assert result == 5


def test_count_no_vowels(non_vowels):
    print(non_vowels)
    result = VowelsCounter.count_vowels(non_vowels)
    assert result == 0
