from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import codecs
import re
import requests

# URL = "https://www.google.com/search?q=nba&oq=nba&aqs=chrome.0.0i271j46i67i131i433j35i39j0i67i131i433l3j0i131i433i512j69i60.879j0j7&sourceid=chrome&ie=UTF-8"
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
#
# matches = soup.find_all(class_="imspo_mt__tt-w")
#
# num = 0
# for i in matches:
#      print(i)
#      num = num + 1
# print(num)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

val = "https://www.google.com/search?q=nba&oq=nba&aqs=chrome.0.0i271j46i67i131i433j35i39j0i67i131i433l3j0i131i433i512j69i60.879j0j7&sourceid=chrome&ie=UTF-8"

wait = WebDriverWait(driver, 10)

driver.get(val)

get_url = driver.current_url

wait.until(EC.url_to_be(val))

if get_url == val:
    page_source = driver.page_source

soup = BeautifulSoup(page_source, features="html.parser")

#keyword = input("Enter a keyword to find instances of in the article:")

time = soup.body.find_all("div", {"class": "imspo_mt__lm-inl imspo_mt__ndl-p imspo_mt__match-status imso-li-w"})
team = soup.body.find_all("div", {"class": "liveresults-sports-immersive__hide-element"})
score = soup.body.find_all("div", {"class": "imspo_mt__tt-w"})

for element in score:
    print(element.string)

# len_match = len(matches)
#
# title = soup.title.text
#
# file = codecs.open('article_scraping.txt', 'a+')
#
# file.write(title + "\n")
#
# file.write("The following are all instances of your keyword:\n")
#
# count = 1
#
# for i in matches:
#     file.write(str(count) + "." + i + "\n")
#     count += 1
#
# file.write("There were " + str(len_match) + " matches found for the keyword.")
#
# file.close()

driver.quit()
