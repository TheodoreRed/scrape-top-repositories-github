# scrape-top-repositories-github
- Automate the process of extracting large amounts of data from Github
- Github has millions of repositories with data associated with it that could be neatly put together
- Using Python, BeautifulSoup, Requests, Pandas, OS
Here are the steps we'll follow
- We're going to scrape https://github.com/topics
- We'll get a list of topics. For each topic, we'll get topic title, topic page URL, topic description
- For each topic, we'll get the top 25 repositories in the topic from the topic page.
- For each repository, we'll grab the repo name, username, stars, and repo URL
- For each topic we'll create a CSV file  in the following format:

```
Repo Name,Username,Stars,Repo URL
```

## Scrape the list of topics from Github
- Use requests to downlaod the pagee
- Use BeautifulSoup to parse and extract info
- Use 3 methods to return a list of titles, descriptions, & URLs
- Use Pandas Dataframe to neatly put together my dictionary of lists

## For each topic in the list, get the top 25 repositories
- Use the method `get_topic_repos(topic_doc):` to get the `<h3>` tags containing title, repository URL, username, & stars
- Create dictionary and use a for loop to fill dict with data from h3 tags
- Put that dictionary into a pandas dataframe return it
- `scrape_topic(topic_url, path):` checks if a csv file with same name exists
- If there is not a file it will call the `get_topic_repos` function to get data and put it into a CSV file
## Putting everything together
- Finally in `def scrape_topics_repos():` I call the method `scrape_topic()` from topic_info.py 
- That will get a list of topic info and use a loop and `iterrows()` to combine the few methods 
- Which will create a directory to put the CSV file for every topic
## Summary
- Scrape a list of topics together
- For each element in list find the top repos and the username, link, and stars associated with each
- After finding associated data, put together in a pandas dataframe and convert to CSV
- Put all the CSV files in a directory of their own
#### Ideas For future work
- Take it a step further and move to the repo link or username link
- Get data on what language is used commonly in a topic, how many watching, how many forks, # of commits
