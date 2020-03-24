import pandas as pd


def web_scrape():
    dfs = pd.read_html('https://www.mohfw.gov.in/')
    return dfs[-1]


if __name__ == "__main__":
    web_scrape()
