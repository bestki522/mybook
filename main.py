from get_post_link import get_post_link
from get_drive_link import get_drive_link
from requests import get
import time

URL = "https://chiasemoi.com/tai-sach/sach-nuoi-day-con/page/{}/"

# initial result in list object
post_link = []
shared_link = []
# run function with 1st, 2nd page
for p in range(1, 3):
    temp_link = get_post_link(URL.format(p))
    post_link.extend(temp_link)

print(post_link)

# run function to get drive shared link from post links
for d in post_link:
    shared_link.append(get_drive_link(d))
    time.sleep(3)

print(shared_link)
print(shared_link.len())
