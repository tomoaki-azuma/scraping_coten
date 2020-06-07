# -*- coding: utf-8 -*-
import os
import re
import csv
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = 'https://www.youtube.com/channel/UCr5zQB5J5DJqZfar_WyWFAw/videos'

driver = webdriver.Chrome('./chromedriver')
driver.get(url)
current_html = driver.page_source
element = driver.find_element_by_xpath('//*[@class="style-scope ytd-page-manager"]')
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
actions.reset_actions()

#最下部までスクロールしたソースを取得
while True:
    for j in range(10):
        actions.send_keys(Keys.PAGE_DOWN)
    actions.perform()
    sleep(3)
    html = driver.page_source
    if current_html != html:
        current_html=html
    else:
        break

ret = []
soup = BeautifulSoup(current_html, 'html.parser')
for link in soup.find_all("a"):
    title = (link.get("title"))
    href = (link.get("href"))
    if title and href:
        if "/watch?v=" in href:
            ret.append([title, href])

with open('temp.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(ret)