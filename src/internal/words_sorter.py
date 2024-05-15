from typing import List, Literal

class WordsSorter:
  @classmethod
  def sort(cls, words: List[str], order: Literal['asc', 'desc']) -> List[str]:
    return sorted(words, reverse=(order == "desc"))
