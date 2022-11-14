import requests
from bs4 import BeautifulSoup
import pandas as pd


topics_url = "https://github.com/topics"
response = requests.get(topics_url)

page_contents = response.text

# Writes page contents copy to local html file
with open("webpage.html", "w", encoding="utf-8") as f:
    f.write(page_contents)

# creates a beautiful soup object, using html file and html parser
doc = BeautifulSoup(page_contents, "html.parser")

topic_title_tags = doc.find_all(
    "p", {"class": "f3 lh-condensed mb-0 mt-1 Link--primary"}
)
# saves the first element's title
# first_element_title = topic_title_tags[0].text
# However I want to save all the titles in a list
topic_titles = []
for tag in topic_title_tags:
    topic_titles.append(tag.text)


topic_desc_tags = doc.find_all("p", {"class": "f5 color-fg-muted mb-0 mt-1"})
# saves the first element's description
# first_element_desc = topic_desc_tags[0].text.strip()
# Saves all title descriptions
topic_descs = []
for tag in topic_desc_tags:
    topic_descs.append(tag.text.strip())


topic_link_tags = doc.find_all("a", {"class": "no-underline flex-grow-0"})
# saves the first element's URL
# first_element_link = "https://github.com" + topic_link_tags[0]["href"]
# Saves all title URLS
topic_links = []
for tag in topic_link_tags:
    topic_links.append("https://github.com" + tag["href"])

# creates a ditionary of the 3 lists I made
topics_dict = {"title": topic_titles, "description": topic_descs, "url": topic_links}

# create a pandas dataframe and put dictionary of lists inside
topics_df = pd.DataFrame(topics_dict)

# transer dataframe into CSV file, index=none so that it doesn't list the index in the csv file
topics_df.to_csv("topics.csv", index=None)


def get_topic_title(doc):
    topic_title_tags = doc.find_all(
        "p", {"class": "f3 lh-condensed mb-0 mt-1 Link--primary"}
    )
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text)
    return topic_titles


def get_topic_desc(doc):
    topic_desc_tags = doc.find_all("p", {"class": "f5 color-fg-muted mb-0 mt-1"})
    topic_descs = []
    for tag in topic_desc_tags:
        topic_descs.append(tag.text.strip())
    return topic_descs


def get_topic_url(doc):
    topic_link_tags = doc.find_all("a", {"class": "no-underline flex-grow-0"})
    topic_links = []
    for tag in topic_link_tags:
        topic_links.append("https://github.com" + tag["href"])
    return topic_links


def scrape_topics():
    topics_url = "https://github.com/topics"
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception("Failed to load page {}".format(topics_url))
    topics_dict = {
        "title": get_topic_title(doc),
        "description": get_topic_desc(doc),
        "url": get_topic_url(doc),
    }
    return pd.DataFrame(topics_dict)
