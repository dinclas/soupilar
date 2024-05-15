from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

from ..internal.vowels_counter import VowelsCounter

router = APIRouter()

class WordsPayload(BaseModel):
    words: List[str]

@router.post("/vowel_count")
async def vowel_count(payload: WordsPayload):
    vowel_counts = {word: VowelsCounter.count_vowels(word) for word in payload.words}

    return vowel_counts

