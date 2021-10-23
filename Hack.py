import requests
from bs4 import BeautifulSoup
import time


while(True):
    source = requests.get("https://www.worldometers.info/world-population/us-population/").text

    time.sleep(1)

    soup = BeautifulSoup(source,'html5lib')

    mainCounter = soup.find("div", class_="table-responsive")


    var = mainCounter.find("strong").text
    
    print(var)
