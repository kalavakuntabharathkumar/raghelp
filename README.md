# Agentic RAG Support Assistant for Enterprise Helpdesk

A runnable, educational PoC for enterprise helpdesk retrieval. It includes document chunking, a FAISS vector index when installed (with a deterministic TF-IDF fallback), a small tool-calling agent loop, FastAPI endpoints, evaluation on labelled sample queries, and pytest coverage.

## Quick start (Python 3.10–3.12 recommended)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`. Ask a question with `POST /ask`, inspect documents with `GET /documents`, and run `python -m app.evaluate`.

Optional LLM: set `OPENAI_API_KEY` and `OPENAI_MODEL` in your environment to enable OpenAI answer generation. Without a key, the app uses an extractive answer so it runs locally. Never commit secrets. FAISS and Hugging Face dependencies are optional; the baseline fallback keeps the project runnable on ordinary laptops.

## Architecture

1. `app/ingest.py` normalizes and chunks the helpdesk knowledge base.
2. `app/retrieval.py` embeds chunks with TF-IDF by default and uses FAISS when optional dependencies and a compatible embedding setup are installed.
3. `app/agent.py` routes between retrieval, clarification, and escalation tools; retrieved context is treated as untrusted data.
4. `app/generation.py` generates a grounded answer and cites document IDs.
5. `app/evaluate.py` scores labelled questions using keyword-supported answer checks. The included tiny dataset is illustrative, not evidence for the resume metrics.

## API

- `GET /health`
- `GET /documents`
- `POST /ask` with `{"question":"How do I reset my password?"}`
- `POST /feedback` with `{"question":"...", "helpful": true}`

## Notes

This is a portfolio PoC, not a production helpdesk system. For production, add access control, tenant-aware filtering, PII handling, prompt-injection defenses, observability, real labelled evaluation data, rate limits, and an AWS deployment pipeline. `Dockerfile` and `infra/` provide starter deployment assets; AWS resources are not provisioned automatically.
