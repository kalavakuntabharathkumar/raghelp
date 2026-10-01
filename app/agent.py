"""A small tool-routing loop: retrieve, clarify, or escalate."""
from .generation import answer_question

class SupportAgent:
    def __init__(self, retriever): self.retriever=retriever
    def run(self, question):
        question=question.strip()
        if len(question)<5:
            return {"answer":"Could you share a little more detail so I can find the right helpdesk guidance?","route":"clarify","sources":[]}
        q=question.lower()
        urgent=any(term in q for term in ("account compromised","security incident","company-wide outage","production outage"))
        hits=self.retriever.search(question,k=3)
        if urgent:
            return {"answer":"This may need urgent human attention. Contact the IT/security service desk now and include the impact and observed time; do not share passwords or recovery codes.","route":"escalate","sources":[h["id"] for h in hits]}
        answer=answer_question(question,hits)
        return {"answer":answer,"route":"retrieve" if hits else "no_match","sources":[h["id"] for h in hits]}
