from bs4 import BeautifulSoup
import requests


def get_drive_link(page):
    """Get book drive link and return string object"""

    html_content = requests.get(page).text  # get html content in text format
    soup = BeautifulSoup(html_content, 'html.parser')  # parse html text content to bs4 object
    gd = str()
    # get all <a> tag with <href not null> and text equal "PDF"
    for h in soup.findAll('a', href=True, text="PDF"):
        if h.text:
            gd = h['href']
    return gd


#print(get_drive_link("https://chiasemoi.com/chien-luoc-cua-me-thay-doi-cuoc-doi-con.html"))
