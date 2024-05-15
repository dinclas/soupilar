from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel, conlist
from typing import Literal

from ..internal.vowels_counter import VowelsCounter
from ..internal.words_sorter import WordsSorter

router = APIRouter()


# Return HTTP 415 if Content-Type is not application/json
def validate_content_type(request: Request):
    if request.headers.get("Content-Type") != "application/json":
        raise HTTPException(
            status_code=415, detail="Unsupported Media Type. Use application/json."
        )


class WordsPayload(BaseModel):
    words: conlist(str, min_length=1)


class SortPayload(WordsPayload):
    order: Literal["asc", "desc"]


@router.post("/vowel_count", dependencies=[Depends(validate_content_type)])
async def vowel_count(payload: WordsPayload):
    return {word: VowelsCounter.count_vowels(word) for word in payload.words}


@router.post("/sort", dependencies=[Depends(validate_content_type)])
async def sort_words(payload: SortPayload):
    return WordsSorter.sort(payload.words, payload.order)
