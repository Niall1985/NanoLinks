import string
import random
from flask import Flask, redirect, request, render_template

app = Flask(__name__)


def generate_shortened_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

@app.route('/', methods = ['GET'])
def index():
    return render_template('Index.html')

@app.route('/shorten', methods = ['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = generate_shortened_url()
    return render_template('Index.html', short_url = short_url)

if __name__ == "__main__":
    app.run(debug=True)