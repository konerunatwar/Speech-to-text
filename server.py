from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import needle
import tempfile
import os

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...), language: str = Form("auto")):
    data = await audio.read()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(data)
        path = f.name
    try:
        opts = {} if language == "auto" else {"language": language}
        result = needle.transcribe(path, **opts)
        return {"text": result.get("text", ""), "language": result.get("language", "")}
    finally:
        os.unlink(path)
