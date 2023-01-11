""" Test the lipila view function"""

""" test the projects view function"""
def test_lipila_project(client):
    """ test lipila route"""
    response = client.get('/zyambo/projects/lipila')
    assert response.status_code == 200
    assert b'<h2>Collect Fees Online From Students</h2>' in response.data