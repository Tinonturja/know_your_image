# importing libraries
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def get_the_page(url:str):
    # img_url list
    img_url_list = []
    # headers
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    # get the page
    responses = requests.get(url, headers=headers, timeout = 10)
    responses.raise_for_status()

    content = BeautifulSoup(responses.text, "html.parser")
    images = content.find_all('img')
    for img in images:
        src = img.get('src')

        if not src:
            continue

        full_url = urljoin(url,src)

        if any(x in full_url.lower() for x in[

            'icon',
            'logo',
            'static',
            ".svg"
        ]):
            continue
        if full_url.lower().endswith(('jpg', 'jpeg', 'png', 'svg')):
            img_url_list.append(full_url)
        
    return img_url_list

