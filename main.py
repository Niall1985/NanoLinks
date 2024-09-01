import string
import random
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

url_map = {}

def generate_shortened_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

@app.route('/', methods = ['GET'])
def index():
    return render_template('Index.html')

@app.route('/shorten', methods = ['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = generate_shortened_url()
    url_map[short_url] = original_url
    return render_template('Index.html', short_url = short_url)

@app.route('/<short_url>')
def retreive_original_url(short_url):
    original_url = url_map.get(short_url)
    if original_url:
        return redirect(original_url)
    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)