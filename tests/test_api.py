from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health():
 r=client.get('/health'); assert r.status_code==200 and r.json()['status']=='ok'
def test_documents():
 r=client.get('/documents'); assert r.status_code==200 and len(r.json())>=5
def test_password_question():
 r=client.post('/ask',json={'question':'How do I reset my password?'})
 assert r.status_code==200 and 'KB-001' in r.json()['sources']
def test_short_question_clarifies():
 assert client.post('/ask',json={'question':'VPN'}).json()['route']=='clarify'
def test_urgent_question_escalates():
 assert client.post('/ask',json={'question':'My account compromised today'}).json()['route']=='escalate'
def test_empty_question_rejected():
 assert client.post('/ask',json={'question':''}).status_code==422
def test_feedback_is_not_persisted():
 r=client.post('/feedback',json={'question':'VPN','helpful':True})
 assert r.status_code==200 and r.json()['accepted'] is True
