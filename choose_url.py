# importing libraries
from bs4 import BeautifulSoup
import requests

def get_the_page(url:str):
    # img_url list
    img_url_list = []
    # headers
    headers = {"User-Agent": "Mozila/5.0"}
    # get the url
    url = url
    # get the page
    responses = requests.get(url, headers=headers)
    content = BeautifulSoup(responses.text, "html.parser")
    images = content.find_all('img')
    for img in images:
        img_url_list.append(f"https:/{img['src']}")
    return img_url_list

