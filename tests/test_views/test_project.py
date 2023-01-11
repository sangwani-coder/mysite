""" test the projects view function"""
def test_project(client):
    """ test project route"""
    res_get = client.get('/zyambo/projects')
    res_post = client.post('/zyambo/projects')
    assert res_get.status_code == 200
    assert res_post.status_code == 200