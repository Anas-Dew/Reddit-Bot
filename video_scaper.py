from bs4 import BeautifulSoup
import requests
from cprint import *

def linksOfTopVideos(subReddit: str):
    links = []
    URL = f'https://www.reddit.com/r/{subReddit}/'

    # Page content from Website URL
    cprint.info(f'Getting links of top videos from {subReddit}')
    while len(links) == 0:
        page = requests.get( URL )
        # parse html content
        soup = BeautifulSoup( page.content , 'html.parser')

        element = soup.find_all("a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
        for i in element:
            links.append(i.get('href'))
        if len(links) == 0:
            cprint.err('No videos fetched. Trying again...')

    cprint.ok('Completed..!')
    return links

if __name__ == "__main__" :
    ex = linksOfTopVideos('funnyvideos')
    for i in ex:
        print(i)