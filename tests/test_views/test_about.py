""" Test the about function view"""

def test_about(client):
    """ test about route"""
    res = client.get('/zyambo/about')
    assert res.status_code == 200