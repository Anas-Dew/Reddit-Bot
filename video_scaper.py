from bs4 import BeautifulSoup
import requests

def linksOfTopVideos(subReddit: str):
    # Website URL
    # URL = f'https://www.reddit.com/search/?q={searchTerm}'
    URL = f'https://www.reddit.com/r/{subReddit}/'

    # Page content from Website URL
    page = requests.get( URL )

    # parse html content
    soup = BeautifulSoup( page.content , 'html.parser')

    element = soup.find_all("a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    links = []
    for i in element:
        links.append(i.get('href'))
    return links

if __name__ == "__main__" :
    ex = linksOfTopVideos('funnyvideos')
    for i in ex:
        print(i)