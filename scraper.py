import pandas as pd

dfs = pd.read_html('https://www.mohfw.gov.in/')

for df in dfs:
    print(df.to_json(orient='table').replace(r'\/', r'/')\
        .replace(r'S. No.', r'id')\
        .replace(r'Name of State / UT', r'state')\
        .replace(r'Total Confirmed cases (Indian National)', r'confirmIndian')\
        .replace(r'Total Confirmed cases ( Foreign National )', r'confirmForeign')\
        .replace(r'Cured/Discharged/Migrated', r'recovered')\
        .replace(r'Death', r'death'))
