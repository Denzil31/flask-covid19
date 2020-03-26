from flask import Flask, Response, escape, jsonify, request
from flask_cors import CORS

from scraper import web_scrape

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/api')
def api():
    data = web_scrape()
    json_data = data.to_json(orient='table')\
        .replace(r'\/', r'/')\
        .replace(r'S. No.', r'id')\
        .replace(r'Name of State / UT', r'state')\
        .replace(r'Total Confirmed cases (Indian National)', r'confirmIndian')\
        .replace(r'Total Confirmed cases ( Foreign National )', r'confirmForeign')\
        .replace(r'Cured/Discharged/Migrated', r'recovered')\
        .replace(r'Death', r'death')
    return Response(json_data, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)
