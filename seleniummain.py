import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.request import urlopen
import urllib
import re
from requests_html import HTMLSession
from selenium import webdriver


def target_id_enter():
    while True:
        global target_id
        try:
            target_id = int(input("Enter target id: "))
            discord_id_website()
        except ValueError:
            print("Target id needs to be an integer")


def discord_id_website():
    global target_id
    begining_of_url = "https://lookup.guru/"
    whole_url = begining_of_url + str(target_id)
    webbrowser.open(whole_url)
    WEBDRIVER_PATH = './'
    driver = webdriver.Firefox(WEBDRIVER_PATH)
    driver.get(whole_url)
    driver.quite()


target_id_enter()
