import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.request import urlopen
import urllib
import re
from requests_html import HTMLSession
from selenium import webdriver
from seleniumwire import webdriver
import wget


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
    session = HTMLSession()
    WEBDRIVER_PATH = './'
    driver = webdriver.Firefox(WEBDRIVER_PATH)
    begining_of_url = "https://lookup.guru/"
    whole_url = begining_of_url + str(target_id)
    driver.get(whole_url)
    #webbrowser.open(whole_url)
    page = session.get(whole_url)
    page.html.render()
    page.html.html
    print(driver.title)
    proxy_username = "USER_NAME"
    proxy_password = "PASSWORD"
    proxy_url = "Any Website URL"
    proxy_port = 8080
    images = driver.find_elements_by_tag_name('img')
    options = {
        "proxy": {
            "http": f"http://{proxy_username}:{proxy_password}@{proxy_url}:{proxy_port}",
            "verify_ssl": False,
            },
            }
    for image in images:
        global pfp
        pfp = (image.get_attribute('src'))
        break
    print(pfp)
    #763797441275232307
    #img_data = requests.get(pfp).content
    #with open('icon.png', 'wb') as handler:
    #handler.write(img_data)
    

target_id_enter()
