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
# h3_tag = result of soup searching a <h3> tag
# star_tag = result of soup searching a <span> tag
def get_repo_info(h3_tag, star_tag):
    a_tags = h3_tag.find_all("a")
    username = a_tags[0].text.strip()
    repo = a_tags[1].text.strip()
    url = base_url + a_tags[1]["href"]
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

    # Get h3 tag containing title, repo_url, username
    username_repo_tags = topic_doc.find_all(
        "h3", {"class": "f3 color-fg-muted text-normal lh-condensed"}
    )
    # Get star tags
    project_stars = topic_doc.find_all("span", {"class": "Counter js-social-count"})

    # Get repo information
    topic_repos_dict = {"username": [], "repo_name": [], "repo_url": [], "stars": []}
    for i in range(len(username_repo_tags)):
        repo_info = get_repo_info(username_repo_tags[i], project_stars[i])
        topic_repos_dict["username"].append(repo_info[0])
        topic_repos_dict["repo_name"].append(repo_info[1])
        topic_repos_dict["repo_url"].append(repo_info[2])
        topic_repos_dict["stars"].append(repo_info[3])
    return pd.DataFrame(topic_repos_dict)


def scrape_topic(topic_url, path):
    if os.path.exists(path):
        print("The file {} already exists. Skipping...".format(path))
        return
    topic_df = get_topic_repos(get_topic_page(topic_url))
    topic_df.to_csv(path, index=None)


def scrape_topics_repos():
    print("Scraping list of topics.")
    topics_df = topic_info.scrape_topics()

    # Create Directory to put CSV files
    dir_name = "data"
    os.makedirs(dir_name, exist_ok=True)

    for index, row in topics_df.iterrows():
        print('Scraping top repositories for "{}"'.format(row["title"]))
        scrape_topic(row["url"], dir_name + "/{}.csv".format(row["title"]))


scrape_topics_repos()