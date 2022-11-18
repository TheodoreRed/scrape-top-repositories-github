import requests
from bs4 import BeautifulSoup
import pandas as pd

# Searches the bs4 doc for p tags, and a specific class selector.
# Loops through soup object containing title.
# Returns a list of each element's text which in this case is the title.
def get_topic_title(doc):
    topic_title_tags = doc.find_all(
        "p", {"class": "f3 lh-condensed mb-0 mt-1 Link--primary"}
    )
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text.strip())
    return topic_titles


# Searches the bs4 doc for p tags, and a specific class selector.
# Loops through soup object containing description.
# Returns a list of each element's text which in this case is the description of title.
def get_topic_desc(doc):
    topic_desc_tags = doc.find_all("p", {"class": "f5 color-fg-muted mb-0 mt-1"})
    topic_descs = []
    for tag in topic_desc_tags:
        topic_descs.append(tag.text.strip())
    return topic_descs


# Searches the bs4 doc for a tags, and a specific class selector.
# Loops through soup object containing links/urls.
# Returns a list of our base url (+) each element's key at tag["href"]
# example - tag["href"] could look like /topics/bootstrap or /topics/cpp
def get_topic_url(doc):
    topic_link_tags = doc.find_all("a", {"class": "no-underline flex-grow-0"})
    topic_links = []
    for tag in topic_link_tags:
        topic_links.append("https://github.com" + tag["href"])
    return topic_links


# Combines all functions to return a dataframe of topic information
# Returns a pandas dataframe
def scrape_topics():
    topics_url = "https://github.com/topics"
    response = requests.get(topics_url, headers={"User-Agent": "Mozilla/5.0"})

    # If the request fails then stops the program
    if response.status_code != 200:
        raise Exception("Failed to load page {}".format(topics_url))

    with open("topics_html_source.html", "r", encoding="utf-8") as f:
        html_str = f.read()
    # Creates bs4 object to be passed to get 3 pieces of information in a dictionary
    doc = BeautifulSoup(html_str, "html.parser")
    topics_dict = {
        "title": get_topic_title(doc),
        "description": get_topic_desc(doc),
        "url": get_topic_url(doc),
    }
    # Passes dictionary and returns a pandas dataframe
    return pd.DataFrame(topics_dict)
