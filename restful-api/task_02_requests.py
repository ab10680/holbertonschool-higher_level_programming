#!/usr/bin/env python3
"""
task_02_requests.py
Fetch and process data from a public API using Python requests.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from the JSONPlaceholder API and print their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts and save selected fields (id, title, body) into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        filtered = [{'id': p['id'], 'title': p['title'], 'body': p['body']}
                    for p in posts]

        with open('posts.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(filtered)
