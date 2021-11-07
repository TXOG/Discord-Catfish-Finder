import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.request import urlopen
import urllib
import re
from requests_html import HTMLSession


def target_id_enter():
    chromiumdownload = input(
        "This program will need to install chromium into your home directory, are you ok with this? (y, yes, n, no): ")
    if chromiumdownload == ("yes"):
        chromiumdownload = ("y")
    if chromiumdownload == ("y"):
        while True:
            global target_id
            try:
                target_id = int(input("Enter target id: "))
                discord_id_website()
            except ValueError:
                print("Target id needs to be an integer")
    else:
        end = input("press any key to terminate the program")
        exit()


def discord_id_website():
    global target_id
    session = HTMLSession()
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
              'AppleWebKit/537.11 (KHTML, like Gecko) '
              'Chrome/23.0.1271.64 Safari/537.11',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
              'Accept-Encoding': 'none',
              'Accept-Language': 'en-US,en;q=0.8',
              'Connection': 'keep-alive'}
    begining_of_url = "https://lookup.guru/"
    whole_url = begining_of_url + str(target_id)
    webbrowser.open(whole_url)
    page = session.get(whole_url)
    page.html.render()
    print("done")


def getHTMLdocument(url):

    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


target_id_enter()
