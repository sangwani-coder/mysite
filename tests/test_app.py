#!/usr/bin/env python3
""" tests the app module"""
import pytest

class TestStatusCodes:
    def test_PageNotFound(self, client):
        """ tests error 404"""
        res1 = client.get('/zyambo/api')
        res2 = client.get('/zyambo/')
        res3 = client.get('/about')
        assert res1.status_code == 404
        assert res2.status_code == 404
        assert res3.status_code == 404

    def test_status(self, client):
        """ tests status 200"""
        response = client.get('/status')
        assert response.status_code == 200

    def test_MethodNotAllowed(self, client):
        """ tests unauthorized methods"""
        res1 = client.post('/')
        res2 = client.post('/zyambo/about')
        assert res1.status_code == 405
        assert res2.status_code == 405
    
    def test_index(self, client):
        """ test the index route"""
        res = client.get('/')
        assert res.status_code == 200

    def test_about(self, client):
        """ test about route"""
        res = client.get('/zyambo/about')
        assert res.status_code == 200

    def test_contact(self, client):
        """ test contact route"""
        res_get = client.get('/zyambo/contact')
        res_post = client.post('/zyambo/contact')
        assert res_get.status_code == 200
        assert res_post.status_code == 200

    def test_project(self, client):
        """ test project route"""
        res_get = client.get('/zyambo/projects')
        res_post = client.post('/zyambo/projects')
        assert res_get.status_code == 200
        assert res_post.status_code == 200