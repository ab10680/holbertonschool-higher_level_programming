#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return None

def read_csv_file():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return [dict(row) for row in reader]
    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    data = []

    if source == 'json':
        data = read_json_file()
    elif source == 'csv':
        data = read_csv_file()
    else:
        error = "Wrong source"

    if data is None:
        error = "Could not read data"

    if not error and product_id:
        filtered = [item for item in data if str(item.get('id')) == str(product_id)]
        if not filtered:
            error = "Product not found"
        else:
            data = filtered

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
