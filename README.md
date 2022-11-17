# scrape-top-repositories-github
## What does it do?
- Automates the process of extracting data from all topics on `https://github.com/topics` into a CSV file in the form:
```
title,description,url
```
- That will get me roughly 180 topics to get the top 20 repositories from each. Each repository will save a CSV file in the form:
```
username,repo_name,repo_url,stars
```
Working on a way to let users interact with the data it provides on a basic level

## Packages you'll need to install 
- `pip install selenium`
- `pip install beautifulsoup4`
- `pip install requests`
- `pip install pandas`

## How it works

# Credit
- Used this [__Base Source Code__](https://jovian.ai/aakashns-6l3/scraping-github-topics-repositories) while following the [__Jovian Python Web Scraping Project__](https://www.youtube.com/watch?v=RKsLLG-bzEY&t=808s) youtube video.
- Stack Overflow [__question__](https://stackoverflow.com/questions/74464469/how-to-use-python-with-selenium-to-click-the-load-more-button-on-https-gith/74465575#74465575) about clicking load more was answered by [__Prophet__](https://stackoverflow.com/users/3485434/prophet?tab=profile)

