import pytest
from ..words_sorter import WordsSorter


@pytest.fixture
def words():
    return ["batman", "robin", "coringa"]


@pytest.fixture
def ascii_values():
    return ["".join(chr(r)) for r in range(0, 256)]


def test_sorts_asc(words):
    result = WordsSorter.sort(words, "asc")
    assert result == ["batman", "coringa", "robin"]


def test_sorts_desc(words):
    result = WordsSorter.sort(words, "desc")
    assert result == ["robin", "coringa", "batman"]


def test_sorts_ascii_asc(ascii_values):
    result = WordsSorter.sort(ascii_values, "asc")
    assert result == ascii_values


def test_sorts_ascii_desc(ascii_values):
    result = WordsSorter.sort(ascii_values, "desc")
    assert result == list(reversed(ascii_values))
