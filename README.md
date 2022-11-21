# scrape-top-repositories-github
## What does it do?
- Automates the process of extracting the top 20 repositories in each topic on `https://github.com/topics`.
- Takes in user input to interact with the created data.
# Get it to work
These are all the packages you'll need install.
- `pip install selenium`
- `pip install beautifulsoup4`
- `pip install requests`
- `pip install pandas`
### After installing packages
1. Run the file `RUN_SCRAPER.py` to extract data and create local files of it.
2. Next, run the file `use_the_data.py` to interact with the data via the command line.
## Known Issues
- `RUN_SCRAPER.py` will fail from making too many requests, and as a result only a portion of the data will be available until its run multiple times and the program can reach an end.
# Credit
- Used this [__Base Source Code__](https://jovian.ai/aakashns-6l3/scraping-github-topics-repositories) while following the [__Jovian Python Web Scraping Project__](https://www.youtube.com/watch?v=RKsLLG-bzEY&t=808s) youtube video.
- Stack Overflow [__question__](https://stackoverflow.com/questions/74464469/how-to-use-python-with-selenium-to-click-the-load-more-button-on-https-gith/74465575#74465575) about clicking load more was answered by [__Prophet__](https://stackoverflow.com/users/3485434/prophet?tab=profile)

