from flask import Flask, escape, request, jsonify
from scraper import web_scrape
app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/api')
def api():
    data = web_scrape()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
