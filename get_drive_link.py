from bs4 import BeautifulSoup
import requests
import re


def get_drive_link(page):
    """Get book drive link and return string object"""

    html_content = requests.get(page).text  # get html content in text format
    soup = BeautifulSoup(html_content, 'html.parser')  # parse html text content to bs4 object
    gd = str()
    # get all <a> tag with <href not null> and text exact match "PDF" or "Here"
    # for h in soup.findAll('a', href=True, text="PDF"):
    for h in soup.findAll('a', href=True, text=re.compile(r'^PDF|^Here')):
        if h.text:
            gd = h['href']
    return gd

#print(get_drive_link("https://chiasemoi.com/thuc-don-an-dam-kieu-nhat-cho-be-5-15-thang-tuoi.html"))
#print(get_drive_link("https://chiasemoi.com/suc-manh-cua-viec-dat-cau-hoi-dung.html"))
