# -*- coding: utf-8 -*-
"""The news command."""


from json import dumps
import requests
import bs4
from .base import Base

class News(Base):
    """Stay connected to Pikachu!"""

    def run(self):
        print "Fetching latest pikachu news... just for you..\n"

        page = requests.get('https://www.ndtv.com/topic/pikachu')
        #print page
        soup = bs4.BeautifulSoup(page.content, "lxml")

        soup = soup.find(id="news_list")
        #soup = soup.find_all("div")[2]

        all_news = soup.find_all("li")

        lim = 0
        for new in all_news:
            attr = new.find_all("p")
            if attr[0].string != None:
                print "\033[1mTitle:\033[0m "+attr[0].string.strip()
                print "\033[1mLink:\033[0m \033[3m"+attr[0].a.get("href")+"\033[3m"
            if attr[1].string != None:
                print "\033[1mDate:\033[0m "+attr[1].string.strip().split("|")[1]
            if attr[3].string != None:
                print "\033[1mSummary:\033[0m "+attr[3].string.strip()
            lim = lim+1
            if lim > 4:
                break
            print"\n\n"

        print "\nPika pika ϞϞ(๑⚈ ․̫ ⚈๑)∩\n"
