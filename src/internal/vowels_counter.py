class VowelsCounter:
    VOWELS = "aeiou"

    @classmethod
    def count_vowels(cls, word: str) -> int:
        return sum(1 for char in word.lower() if char in cls.VOWELS)
