

from selenium import webdriver  # required for scrape inspect links
from bs4 import BeautifulSoup as bs  # required for scrape inspect links
import re  # required for transform to download links



scrapeurl="https://www.twitch.tv/directory/game/Just%20Chatting/clips?range=7d"
options = webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(firefox_options=options)  # replace with .Firefox(), or with the browser of your choice
url = str(scrapeurl)
browser.get(url)  # navigate to the page
uglyhtml = browser.page_source
browser.close()

soup = bs(uglyhtml, "html.parser")


links1 = ""
for link in soup.find_all("img"):
    print(link)


    links1 = str(links1) + str(link.get("src") + "\n")
links1 = links1.splitlines()

# scrapes links using regex:
# . - any character that is not new line
# * - repeat prievious option 0 or more times
# ? - dont be greedy
# 7C the start of constant strint
# (.*) group1 collection inside () again select anything 0 or more times
# \-p escape - key, follow up with p for a -p end of quirey
# skip everything till the end line with .* as prieviously
full_links = ""
for link2 in links1:
    m = re.match(r".*?7C(.*)\-p.*", link2)
    if m != None:
        full_links = full_links + ("https://clips-media-assets2.twitch.tv/AT-cm%7C" + m.group(1) + "-360" + ".mp4\n")
full_links = full_links.splitlines()


# returns array of downloadable links
