""" Test the index view function"""

def test_index(client):
    """ test the index route"""
    res = client.get('/')
    assert res.status_code == 200