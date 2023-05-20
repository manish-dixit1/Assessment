import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_unique_words(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text().lower()
    words = text.split()
    word_counts = Counter(words)
    unique_words = [{'word': word, 'count': count} for word, count in word_counts.items()]
    return unique_words

@app.route('/analyze', methods=['POST'])
def analyze_website():
    data = request.get_json()
    url = data['url']
    unique_words = get_unique_words(url)
    return jsonify(unique_words)

if __name__ == '__main__':
    app.run()
