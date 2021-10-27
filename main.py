from get_post_link import get_post_link
from get_drive_link import get_drive_link
from converter import get_direct_url
from requests import get
import time

URL = "https://chiasemoi.com/tai-sach/sach-nuoi-day-con/page/{}/"

# initial result in list object
post_link = []
shared_link = []
download_link = []
# run function with 1st, 2nd page
for p in range(1, 3):
    temp_link = get_post_link(URL.format(p))
    post_link.extend(temp_link)

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
print('\n'.join(str(x) for x in download_link))
