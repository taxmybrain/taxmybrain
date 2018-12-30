import pytest


def test_index(client):
    response = client.get('/')
    assert b"Brain Tumour Research" in response.data
    response = client.get('/index')
    assert b"Brain Tumour Research" in response.data