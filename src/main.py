from fastapi import FastAPI
from .routers import words

app = FastAPI()
app.include_router(words.router)

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}