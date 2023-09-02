# import pytest

# from app import create_app

# @pytest.fixture
# def client():
#     app = create_app()
#     app.config['TESTING'] = True

#     with app.test_client() as client:
#         yield client

# def test_home(client):
#     rv = client.get('/')
#     assert b'Hello, World!' in rv.data

# def test_get_data(client):
#     rv = client.get('/api/data')
#     assert b'Some data here' in rv.data
