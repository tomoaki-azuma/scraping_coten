import csv
import re

URL = 'https://www.youtube.com/channel/UCr5zQB5J5DJqZfar_WyWFAw'

with open('temp.csv') as f:
    reader = csv.reader(f)
    ret = []
    for row in reader:
        title = row[0]
        url = row[1]
        m = re.match(r'.+【COTEN RADIO #(\d+)】', title)
        if m:
            ret.append([m.group(1).zfill(3), url])
        
        m = re.match(r'.+【COTEN RADIO\s*番外編 #(\d+)】', title)
        if m:
            ret.append(['ex' + m.group(1).zfill(3), url])

ret = sorted(ret, key=lambda x: x[0])

with open('youtube_url.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(ret)