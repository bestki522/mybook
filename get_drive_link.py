from bs4 import BeautifulSoup
import requests


def get_drive_link(post):
    """Get book drive link and return string object"""

    global drive_link
    html_content = requests.get(post).text  # get html content in text format
    soup = BeautifulSoup(html_content, 'html.parser')  # parse html text content to bs4 object

    links_with_text = []  # initial list of post links

    # get all <a> tag with <href not null> and text equal "PDF"
    for h in soup.findAll('a', href=True, text="PDF"):
        if h.text:
            drive_link = h['href']
    return drive_link


print(get_drive_link("https://chiasemoi.com/chien-luoc-cua-me-thay-doi-cuoc-doi-con.html"))
