# importing libraries
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def get_the_page(url:str):
    # img_url list
    img_url_list = []
    # headers
    headers = {"User-Agent": "Mozila/5.0"}
    # get the page
    responses = requests.get(url, headers=headers)
    responses.raise_for_status()

    content = BeautifulSoup(responses.text, "html.parser")
    images = content.find_all('img')
    for img in images:
        src = img.get('src')
        if src and src.endswith(('jpg', 'jpeg', 'png', 'svg')):
            full_url = urljoin(url,src)
            img_url_list.append(full_url)
        
    return img_url_list

