import re

link1 = "https://drive.google.com/file/d/1j4pMTjSln78axgLmPfxsNiAskcCYk9YJ/view?usp=sharing"
link2 = "https://drive.google.com/open?id=1o4qzqjx2D58wW1jkZd6xV-GvRFOhZbr-"
link3 = "https://drive.google.com/"


def get_direct_url(url, match_object=None):
    """ get file id from drive file url"""

    Download = "https://drive.google.com/u/0/uc?id={}&export=download"
    pattern1 = r"drive\.google\.com\/file\/d\/(.*?)\/"
    pattern2 = r"drive\.google\.com\/open\?id\=(.*)"
    regexList = [pattern1, pattern2]

    for regex in regexList:
        file_id = re.search(regex, url)
        if file_id is not None:
            f = file_id.group(1)
            return Download.format(f)

#print(get_direct_url(link1))
#print(get_direct_url(link2))
#print(get_direct_url(link3))
#print(get_file_id(link2))
#print(get_file_id(link3))
# get_file_id(link2)
# et_file_id(link1)
