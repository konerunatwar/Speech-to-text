# Whistle Speech-to-Text

Speech-to-text prototype using Cactus Compute Whistle through `cactus-needle` and FastAPI.

## Local run

```bash
pip install -r requirements.txt
uvicorn server:app --host 127.0.0.1 --port 8000
```

## Railway

Connect this repository as a Railway service, then generate an HTTPS domain. `railway.json` provides the start command and health check.

**Note:** `cactus-needle` Linux/Railway support and its transcription API have not been validated yet. Deployment and runtime operation are not guaranteed.
