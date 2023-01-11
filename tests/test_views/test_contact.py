""" tests the about function view"""

def test_contact(client):
    """ test contact route"""
    res_get = client.get('/zyambo/contact')
    res_post = client.post('/zyambo/contact')
    assert res_get.status_code == 200
    assert res_post.status_code == 200