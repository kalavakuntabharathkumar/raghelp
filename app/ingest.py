"""Small, transparent ingestion and chunking pipeline."""
import json, re
from pathlib import Path

def load_documents(path=None):
    path = Path(path) if path else Path(__file__).with_name("knowledge_base.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    return [{**d, "text": re.sub(r"\s+", " ", d["text"]).strip()} for d in data]

def chunk_documents(documents, max_chars=420, overlap=60):
    if max_chars < 1 or overlap < 0 or overlap >= max_chars: raise ValueError("Require max_chars > overlap >= 0")
    chunks=[]
    for doc in documents:
        text=doc["text"]
        if len(text) <= max_chars:
            chunks.append({"id":doc["id"],"title":doc["title"],"text":text})
            continue
        start=0
        while start < len(text):
            end=min(len(text),start+max_chars)
            chunks.append({"id":f'{doc["id"]}-{start}',"title":doc["title"],"text":text[start:end]})
            if end == len(text): break
            start=max(start+1,end-overlap)
    return chunks
