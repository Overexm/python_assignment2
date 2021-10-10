from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "https://coinmarketcap.com"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')


class WebScrapper:

    def getDateByRequest(currencyName):
        some_list = []
        for paragraph in soup.find_all("p"):
            if currencyName in paragraph.get_text():
                some_list.append(paragraph.get_text())
        return some_list


    def getData():
        some_list = []
        for paragraph in soup.find_all("p"):
            some_list.append(paragraph.get_text())
        return some_list