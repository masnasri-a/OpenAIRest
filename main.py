import os, argparse
import openai
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()

openai.api_key = "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"

@app.get('/ask')
def chat(ask:str):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Q: {ask}?\nA:",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
    )
    return response.get('choices')[0].get('text')

@app.get('/')
def redirect():
    return RedirectResponse("/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)