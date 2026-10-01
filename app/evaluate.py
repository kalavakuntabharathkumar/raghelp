"""Tiny labelled evaluation harness; replace examples with reviewed production labels."""
from .agent import SupportAgent
from .retrieval import Retriever
from .ingest import load_documents

CASES=[
 ("How can I reset my password?", "KB-001"),
 ("How do I connect to the VPN?", "KB-002"),
 ("Where do I request a laptop?", "KB-003"),
 ("What should I do with a phishing email?", "KB-004"),
 ("How do I get app permissions?", "KB-005"),
 ("Someone compromised my account", "KB-006"),
]
def evaluate():
 agent=SupportAgent(Retriever(load_documents())); rows=[]
 for question, expected in CASES:
  result=agent.run(question); rows.append({"question":question,"expected":expected,"found":expected in result["sources"],"route":result["route"]})
 accuracy=sum(x["found"] for x in rows)/len(rows)
 return {"count":len(rows),"source_hit_rate":round(accuracy,3),"results":rows}
if __name__ == "__main__":
 print(evaluate())
