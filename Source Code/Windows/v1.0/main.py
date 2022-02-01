import requests
import webbrowser
from selenium import webdriver
import time
import json
from selenium.webdriver.chrome.options import Options

global pfp
pfp = ()


def target_id_enter():
    while True:
        global target_id
        try:
            target_id = int(input("Enter target id: "))
            discord_id_website()
        except ValueError:
            print("Target id needs to be an integer")


def discord_id_website():
    print("Finding user url")
    global pfp
    global target_id
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    begining_of_url = "https://lookup.guru/"
    whole_url = begining_of_url + str(target_id)
    driver.get(whole_url)
    print("Waiting for lookup.guru load")
    time.sleep(5)
    print("Scraping pfp")
    images = driver.find_elements_by_tag_name('img')
    for image in images:
        global pfp
        pfp = (image.get_attribute('src'))
        break
    img_data = requests.get(pfp).content
    with open('pfpimage.png', 'wb') as handler:
        handler.write(img_data)
    print("Searching on yandex images")
    filePath = "pfpimage.png"
    searchUrl = 'https://yandex.com/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json',
              'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = searchUrl + '?' + query_string
    print("Opening reverse image search")
    webbrowser.open(img_search_url)


target_id_enter()
