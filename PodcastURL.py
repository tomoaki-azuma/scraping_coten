import requests
import datetime
import urllib
import shutil
import sys
from bs4 import BeautifulSoup
import os
import re
import csv

ret = []
with open('hoge.txt') as f:
    for s_line in f:
        if re.match(r'.*feed.*', s_line):
            soup = BeautifulSoup(s_line, 'html.parser')
            a_tag = soup.find('a')
            if a_tag:
                tmp_href = a_tag.get('href')
                div = soup.find(class_="e3ZUqe")
                if div:
                    tmp = div.string
                    m = re.match(r'#(.\d+)', tmp)
                    if m:
                        ret.append([m.group(1).zfill(3), tmp_href])
                    m = re.match(r'【番外編 #(\d+)】', tmp)
                    if m:
                        ret.append(['ex' + m.group(1).zfill(3), tmp_href])

ret = sorted(ret, key=lambda x: x[0])

with open('podcast_url.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(ret)


