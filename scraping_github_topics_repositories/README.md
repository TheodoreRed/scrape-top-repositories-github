# Project Outline:

- We're going to scrape https://github.com/topics
- We'll get a list of topics. For each topic, we'll get topic title, toic page URL, topic description
- For each topic, we'll get the top 25 repositories in the topic from the topic page.
- For each repository, we'll grab the repo name, username, stars, and repo URL
- For each topic we'll create a CSV file  in the following format:

```
Repo Name,Username,Stars,Repo URL
```

## Use the requests library to download web pages
- I used  the python code below to download webpage and make a local copy
- with open("webpage.html", "w", encoding="utf-8") as f:
- f.write(page_contents)

## Use Beautiful Soup to parse and extract information
- I found the tags that have the title, description, and URL
- Used simple Soup documentation to get data for one
- Used 3 different loops to put the titile, desc, and url in a list
- Used pandas Dataframe to neatly put together dict of lists

#### Create CSV file with the topic
- Use topics_df.to_csv("topics.csv") 

## Getting Information out of a topic page
Write a single function to :
1. Get the list of topics from the topics page
2. Get the list of top repos from the individual topic pages 
3. For each topic, create a CSV of the top repos for the topic