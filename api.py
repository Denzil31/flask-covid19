from flask import Flask, escape, request, jsonify, Response
from scraper import web_scrape


app = Flask(__name__)


@app.route('/')
def hello():
    dict1 = {"prop1": "p1", "prop2": "p2"}
    return jsonify(dict1)


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