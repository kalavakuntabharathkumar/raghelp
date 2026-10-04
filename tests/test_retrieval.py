import pytest
from app.ingest import chunk_documents, load_documents
from app.retrieval import Retriever

def test_chunk_overlap_and_ids():
 chunks=chunk_documents([{'id':'X','title':'Long','text':'a'*100}],max_chars=40,overlap=10)
 assert len(chunks)==4 and chunks[0]['id']=='X-0'
def test_invalid_chunk_parameters():
 with pytest.raises(ValueError): chunk_documents([],max_chars=10,overlap=10)
def test_retrieval_returns_password_article():
 hits=Retriever(load_documents()).search('forgot password email reset')
 assert hits and hits[0]['id']=='KB-001'
def test_blank_query_returns_no_hits():
 assert Retriever(load_documents()).search('   ')==[]
