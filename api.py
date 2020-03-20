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
    return data.to_json(orient='table').replace(r'\/', r'/')\
        .replace(r'S. No.', r'id')\
        .replace(r'Name of State / UT', r'state')\
        .replace(r'Total Confirmed cases (Indian National)', r'confirmIndian')\
        .replace(r'Total Confirmed cases ( Foreign National )', r'confirmForeign')\
        .replace(r'Cured/Discharged/Migrated', r'recovered')\
        .replace(r'Death', r'death')


if __name__ == "__main__":
    app.run(debug=True)
