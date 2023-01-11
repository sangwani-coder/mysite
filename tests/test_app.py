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
        assert res1.status_code == 405
