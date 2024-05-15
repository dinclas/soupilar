from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Literal

from ..internal.vowels_counter import VowelsCounter
from ..internal.words_sorter import WordsSorter

router = APIRouter()

class WordsPayload(BaseModel):
    words: List[str]

class SortPayload(WordsPayload):
    order: Literal['asc', 'desc']

@router.post("/vowel_count")
async def vowel_count(payload: WordsPayload):
    return {word: VowelsCounter.count_vowels(word) for word in payload.words}

@router.post("/sort")
async def sort_words(payload: SortPayload):
    return WordsSorter.sort(payload.words, payload.order)

