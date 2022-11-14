import topic_info
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

base_url = "https://github.com"


# Given a string number that might end in "k" for thousand
# Returns string as integer
def parse_star_count(star_str):
    star_str = star_str.strip()
    if star_str[-1] == "k":
        return int(float(star_str[0:-1]) * 1000)
    else:
        return int(star_str)


# Returns all the required info about a repository
def get_repo_info(h3_tag, star_tag):

    # 2 child a tags of h3_tags containing username and repository
    a_tags = h3_tag.find_all("a")
    username = a_tags[0].text.strip()
    repo = a_tags[1].text.strip()

    # Creates repositories URL
    url = base_url + a_tags[1]["href"]
    # Gets star tag string and uses parse_star_count() to convert to correct type
    stars = parse_star_count(star_tag.text.strip())
    return username, repo, url, stars


def get_topic_page(topic_url):
    # Download the page
    response = requests.get(topic_url)

    # Check download successful
    if response.status_code != 200:
        raise Exception("Failed to load page {}".format(topic_url))

    # Parse using beautiful soup
    topic_doc = BeautifulSoup(response.text, "html.parser")
    return topic_doc


def get_topic_repos(topic_doc):

    # Searches the bs4 topic doc for all h3 tags, and a specific class selector.
    username_repo_tags = topic_doc.find_all(
        "h3", {"class": "f3 color-fg-muted text-normal lh-condensed"}
    )
    # Searches the bs4 topic doc for all span tags, and a specific class selector. Contains star information
    project_stars = topic_doc.find_all("span", {"class": "Counter js-social-count"})

    # Loops through the number of h3 tags in username_repo_tags
    # Data extracted one by one using get_repo_info() passing a unique h3 tag and unique span tag
    topic_repos_dict = {"username": [], "repo_name": [], "repo_url": [], "stars": []}
    for i in range(len(username_repo_tags)):
        repo_info = get_repo_info(username_repo_tags[i], project_stars[i])
        topic_repos_dict["username"].append(repo_info[0])
        topic_repos_dict["repo_name"].append(repo_info[1])
        topic_repos_dict["repo_url"].append(repo_info[2])
        topic_repos_dict["stars"].append(repo_info[3])
    return pd.DataFrame(topic_repos_dict)


def scrape_topic(topic_url, path):
    # If I already have a CSV file with the same name and directory I skip
    if os.path.exists(path):
        print("The file {} already exists. Skipping...".format(path))
        return
    # get_topic_page() is passed a url from topics.csv file and returnsa BeautifulSoup object
    # get_topic_repos() is passed that bs4 object where it extracts the data
    topic_df = get_topic_repos(get_topic_page(topic_url))
    # Extracted data is converted to a csv file
    topic_df.to_csv(path, index=None)


# This is the function that will run both files
def scrape_topics_repos():
    print("Scraping list of topics.")
    # Uses scrape topics from topic_info.py to get dataframe of topic info
    topics_df = topic_info.scrape_topics()
    # Create CSV of that topic info dataframe
    topics_df.to_csv("topics.csv", index=None)

    # Makes a directoy/folder to put CSV files in, called "data"
    dir_name = "data"
    os.makedirs(dir_name, exist_ok=True)

    # Search my topics dataframe to use scrape_topic for each element
    for index, row in topics_df.iterrows():
        print('Scraping top repositories for "{}"'.format(row["title"]))
        scrape_topic(row["url"], dir_name + "/{}.csv".format(row["title"]))


# Runs scraper
scrape_topics_repos()
