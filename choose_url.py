# importing libraries
from bs4 import BeautifulSoup
import requests

def get_the_page(url:str):
    # headers
    headers = {"User-Agent": "Mozila/5.0"}
    # get the url
    url = url
    # get the page
    responses = requests.get(url, headers=headers)
    return BeautifulSoup(responses.text, "html.parser")

