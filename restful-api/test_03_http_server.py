#!/usr/bin/python3
"""Tests for simple HTTP server"""
import urllib.request
import urllib.error
import json


def test_root():
    """Test if root endpoint returns correct content"""
    response = urllib.request.urlopen("http://localhost:8000/")
    assert response.status == 200
    content = response.read().decode("utf-8").strip()
    assert content == "Hello, this is a simple API!"
    print("Test if root endpoint returns correct content.: OK")


def test_data():
    """Test if data endpoint returns correct JSON"""
    response = urllib.request.urlopen("http://localhost:8000/data")
    assert response.status == 200
    data = json.loads(response.read().decode("utf-8"))
    assert data == {"name": "John", "age": 30, "city": "New York"}
    print("Test if data endpoint returns correct data.: OK")


def test_status():
    """Test if status endpoint returns correct JSON"""
    response = urllib.request.urlopen("http://localhost:8000/status")
    assert response.status == 200
    data = json.loads(response.read().decode("utf-8"))
    assert data == {"status": "OK"}
    print("Test if status endpoint returns correct status.: OK")


def test_undefined():
    """Test if undefined endpoint returns correct 404 JSON error"""
    try:
        urllib.request.urlopen("http://localhost:8000/invalid")
    except urllib.error.HTTPError as e:
        assert e.code == 404
        error = json.loads(e.read().decode("utf-8"))
        assert error == {"error": "Not found"}
        print("Test if undefined endpoint returns correct status.: OK")


if __name__ == "__main__":
    test_root()
    test_data()
    test_status()
    test_undefined()
