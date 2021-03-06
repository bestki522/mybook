from get_post_link import get_post_link
from get_drive_link import get_drive_link
from converter import get_direct_url
from requests import get
import pandas as pd
import time

URL = "https://chiasemoi.com/tai-sach/sach-kinh-te/page/{}/"

# initial result in list object
post_link = []
shared_link = []
download_link = []
# run function with 1st, 2nd page
for p in range(1, 24):
    temp_link = get_post_link(URL.format(p))
    post_link.extend(temp_link)
    time.sleep(1)

print(post_link)
print(len(post_link))

# run function to get drive shared link from post links
for d in post_link:
    shared_link.append(get_drive_link(d))
    time.sleep(2)

print(shared_link)
print(len(shared_link))

for l in shared_link:
    download_link.append(get_direct_url(l))

print(download_link)
# print('\n'.join(str(x) for x in download_link))

pd.DataFrame({'Post': post_link, 'Shared': shared_link, 'Download': download_link}).to_csv('test.csv')
