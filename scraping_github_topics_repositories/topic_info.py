import requests
from bs4 import BeautifulSoup
import pandas as pd

# returns list of the topic's title
def get_topic_title(doc):
    topic_title_tags = doc.find_all(
        "p", {"class": "f3 lh-condensed mb-0 mt-1 Link--primary"}
    )
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text.strip())
    return topic_titles


# returns a list of the topic's description
def get_topic_desc(doc):
    topic_desc_tags = doc.find_all("p", {"class": "f5 color-fg-muted mb-0 mt-1"})
    topic_descs = []
    for tag in topic_desc_tags:
        topic_descs.append(tag.text.strip())
    return topic_descs


# returns a list of the topic's URL
def get_topic_url(doc):
    topic_link_tags = doc.find_all("a", {"class": "no-underline flex-grow-0"})
    topic_links = []
    for tag in topic_link_tags:
        topic_links.append("https://github.com" + tag["href"])
    return topic_links


# Combines above functions to return a pandas dataframe
def scrape_topics():
    topics_url = "https://github.com/topics"
    response = requests.get(topics_url, headers={"User-Agent": "Mozilla/5.0"})

    # If the request fails then stops the program
    if response.status_code != 200:
        raise Exception("Failed to load page {}".format(topics_url))

    # `get_all_html_source.py` outputs the file thats opened here
    with open("topics_html_source.html", "r", encoding="utf-8") as f:
        html_str = f.read()
    doc = BeautifulSoup(html_str, "html.parser")
    topics_dict = {
        "title": get_topic_title(doc),
        "description": get_topic_desc(doc),
        "url": get_topic_url(doc),
    }
    return pd.DataFrame(topics_dict)
