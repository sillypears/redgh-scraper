from bs4 import BeautifulSoup, Tag
import lxml
import requests
import sys
from time import sleep
from random import randint, choice
import os

URL = "https://geekhack.org/index.php?action=recenttopics;xml"
WEBBIE = os.environ.get("me_discord_webbie")
USER = os.environ.get("gh_username")
ME = os.environ.get("me_discord_id")
def main():

    while True:
        xml = requests.get(URL)
        bs_data = BeautifulSoup(xml.content, "xml")
        for x in bs_data.find_all('topic'):
            if "Nightcaps" in x.subject.string:
                bb_data = BeautifulSoup(x.last.string, "xml")
                for y in bb_data:
                    link = y.attrs.get('href')
                    user = y.string
                    if user == USER:
                        print(f"{user} posted {link}")
                        requests.post(WEBBIE, data={"content": f"{user} posted {link} <@{ME}>"})
            bb_data = BeautifulSoup(x.last.string, "xml")
            for w in bb_data:
                if USER == w.string:
                        print(f"{w.string} posted {w.attrs.get('href')}")
                        requests.post(WEBBIE, data={"content": f"{w.string} posted {w.attrs.get('href')} <@83211222777860096>"})
 
        r = randint(3,10)
        print(f"loopin -> {r}")
        sleep(r)     
    return 0

if __name__ == "__main__":
    sys.exit(main())