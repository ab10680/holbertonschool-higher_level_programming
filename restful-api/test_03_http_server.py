#!/usr/bin/env python3
import urllib.request
import json


def test_root():
    with urllib.request.urlopen("http://localhost:8000/") as response:
        body = response.read().decode("utf-8")
        assert body.strip() == "Hello, this is a simple API!"
        print("Test if root endpoint returns correct content.: OK")


def test_data():
    with urllib.request.urlopen("http://localhost:8000/data") as response:
        data = json.loads(response.read().decode("utf-8"))
        assert data == {"name": "John", "age": 30, "city": "New York"}
        print("Test if data endpoint returns correct data.: OK")


def test_status():
    with urllib.request.urlopen("http://localhost:8000/status") as response:
        data = json.loads(response.read().decode("utf-8"))
        assert data == {"status": "OK"}
        print("Test if status endpoint returns correct status.: OK")


def test_undefined():
    try:
        urllib.request.urlopen("http://localhost:8000/doesnotexist")
    except urllib.error.HTTPError as e:
        assert e.code == 404
        error = json.loads(e.read().decode("utf-8"))
        assert error == {"error": "Endpoint not found"}
        print("Test if undefined endpoint returns correct status.: OK")


if __name__ == "__main__":
    test_root()
    test_data()
    test_status()
    test_undefined()
