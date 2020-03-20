import pandas as pd


def web_scrape():
    dfs = pd.read_html('https://www.mohfw.gov.in/')
    return dfs[0]
