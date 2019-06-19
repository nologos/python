from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time 


link="https://www.twitch.tv/tenderlybae/clips?filter=clips&range=7d"
 # used later 



options = webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(firefox_options=options) 
# browser = webdriver.Firefox()

url = str(link)
browser.get(url)

#==============
time.sleep(5)
elements = browser.find_elements_by_class_name("tw-image")

links = ""
for element in elements:
        # print(element.get_attribute('outerHTML')) # this would print  all elements from tw-image
        print(element.get_attribute('src')) # narrowed down selection
        regex_match = re.match(r".*?7C(.*)\-p.*", element.get_attribute('src'))
        if regex_match != None:
                links = links + ("https://clips-media-assets2.twitch.tv/AT-cm%7C" + regex_match.group(1) + ".mp4\n")

links = links.splitlines()

print(links)

# browser.close()


urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=48399): Max retries exceeded with url: /session/ad155bd9-6bae-402a-9b8d-c4401ebb01e1/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f42b19a83c8>: Failed to establish a new connection: [Errno 111] Connection refused',))
