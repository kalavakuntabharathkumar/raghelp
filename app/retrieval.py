"""Retrieval abstraction with deterministic TF-IDF baseline."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .ingest import load_documents, chunk_documents

class Retriever:
    def __init__(self, documents=None):
        self.documents=chunk_documents(documents if documents is not None else load_documents())
        self.vectorizer=TfidfVectorizer(ngram_range=(1,2), stop_words="english")
        self.matrix=self.vectorizer.fit_transform([d["text"] for d in self.documents])
    def search(self, query, k=3):
        if not query.strip(): return []
        q=self.vectorizer.transform([query])
        scores=cosine_similarity(q,self.matrix).ravel()
        order=scores.argsort()[::-1][:k]
        return [{**self.documents[i],"score":float(scores[i])} for i in order if scores[i] > 0]
