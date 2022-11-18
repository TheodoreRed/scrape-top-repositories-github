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

## Packages you'll need to install 
- `pip install selenium`
- `pip install beautifulsoup4`
- `pip install requests`
- `pip install pandas`

## Get it to work
1. Run `get_all_html_source.py` to return a html file locally
2. Next, run `topic_page_info.py`. This will run the scraper.
3. A directory called `data` will be created and .csv files will begin to fill up there.

# Credit
- Used this [__Base Source Code__](https://jovian.ai/aakashns-6l3/scraping-github-topics-repositories) while following the [__Jovian Python Web Scraping Project__](https://www.youtube.com/watch?v=RKsLLG-bzEY&t=808s) youtube video.
- Stack Overflow [__question__](https://stackoverflow.com/questions/74464469/how-to-use-python-with-selenium-to-click-the-load-more-button-on-https-gith/74465575#74465575) about clicking load more was answered by [__Prophet__](https://stackoverflow.com/users/3485434/prophet?tab=profile)

