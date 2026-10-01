from fastapi import FastAPI
from pydantic import BaseModel, Field
from .agent import SupportAgent
from .ingest import load_documents
from .retrieval import Retriever

app=FastAPI(title="Agentic RAG Support Assistant", version="0.1.0", description="Portfolio PoC for grounded helpdesk answers")
retriever=Retriever(load_documents())
agent=SupportAgent(retriever)
class AskRequest(BaseModel): question: str = Field(min_length=1, max_length=2000)
class FeedbackRequest(BaseModel): question: str; helpful: bool
@app.get("/health")
def health(): return {"status":"ok","documents":len(retriever.documents)}
@app.get("/documents")
def documents(): return [{"id":d["id"],"title":d["title"]} for d in load_documents()]
@app.post("/ask")
def ask(payload: AskRequest): return agent.run(payload.question)
@app.post("/feedback")
def feedback(payload: FeedbackRequest):
    # Demo endpoint only; production should persist feedback to a protected data store.
    return {"accepted":True,"helpful":payload.helpful,"message":"Feedback accepted for this demo; it is not persisted."}
