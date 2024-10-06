import pytest
from app.server import create_app, db

@pytest.fixture
def client():
    app = create_app(testing=True) 
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all() 
        yield client
        db.drop_all()  

def test_ask_endpoint(client):
    response = client.post('/ask', json={'question': 'What is the capital of France?'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'question' in data
    assert 'answer' in data
    assert 'Paris' in data['answer']
