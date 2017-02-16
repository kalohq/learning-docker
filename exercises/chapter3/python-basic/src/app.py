#!/usr/bin/python

import random
import requests

from flask import Flask, redirect, render_template

app = Flask(__name__, static_url_path='')

API_KEY = 'dc6zaTOxFJmzC'


@app.route('/')
def entry_point():
    return render_template('index.html')


@app.route('/query/<path:query>')
def what(query):
    # Query Giphy API if there is a query
    response = requests.get(
        'http://api.giphy.com/v1/gifs/search?q={}&api_key={}&limit=10'.format(
            query, API_KEY
        )
    )
    giphy_gifs = response.json()['data']

    # Show the first GIF
    if len(giphy_gifs) > 0:
        return redirect(
            giphy_gifs[
                random.randint(0, 100) % len(giphy_gifs)
            ]['images']['original']['url'],
            code=302
        )
    # Show a failure message
    else:
        return render_template(
            'nogif.html', title='Awww, no GIF for {}'.format(query)
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
