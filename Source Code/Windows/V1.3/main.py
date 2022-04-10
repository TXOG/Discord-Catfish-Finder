import requests
import webbrowser
from selenium import webdriver
import time
import json
import colorama
from colorama import Fore, init
from selenium.webdriver.chrome.options import Options

print("""            _____   _____ ______
           |  __ \ / ____|  ____|
           | |  | | |    | |__
           | |  | | |    |  __|
           | |__| | |____| |
           |_____/ \_____|_|

                       """)

colorama.init()

global pfp
pfp = "a"


def userInput():
    while True:
        global target_id
        try:
            print(Fore.LIGHTBLUE_EX + "\n")
            target_id = int(input("Enter target id: "))
            scraping()
        except ValueError:
            print(Fore.RED + "Target id needs to be an integer")
            print(Fore.WHITE + "\n")


def scraping():
    print(Fore.LIGHTGREEN_EX + "Declaring global variables")
    print(Fore.WHITE)
    global pfp
    global target_id
    print(Fore.LIGHTGREEN_EX + "Setting up Chrome driver")
    print(Fore.WHITE)
    chrome_options = Options()
    print(Fore.LIGHTGREEN_EX + "Applying headless argument")
    print(Fore.WHITE)
    chrome_options.add_argument("--headless")
    print(Fore.LIGHTGREEN_EX + "Creating driver")
    print(Fore.WHITE)
    driver = webdriver.Chrome(options=chrome_options)
    print(Fore.LIGHTGREEN_EX + "Creating url for lookup.guru")
    print(Fore.WHITE)
    begining_of_url = "https://lookup.guru/"
    whole_url = begining_of_url + str(target_id)
    print(Fore.LIGHTGREEN_EX + "Getting url")
    print(Fore.WHITE)
    driver.get(whole_url)
    print(Fore.LIGHTGREEN_EX + "Waiting 5 seconds for lookup.guru to load")
    print(Fore.WHITE)
    time.sleep(5)
    print(Fore.LIGHTGREEN_EX + "Searching for images")
    print(Fore.WHITE)
    images = driver.find_elements_by_tag_name('img')
    print(Fore.LIGHTGREEN_EX + "Scraping images")
    print(Fore.WHITE)
    for image in images:
        global pfp
        pfp = (image.get_attribute('src'))
        break
    print(Fore.LIGHTGREEN_EX + "Checking if user exists")
    print(Fore.WHITE)
    if pfp == "a":
        print(Fore.RED + "User not found")
        print(Fore.WHITE + "\n")
        userInput()
    print(Fore.LIGHTGREEN_EX + "Downloading profile image to ./")
    print(Fore.WHITE)
    img_data = requests.get(pfp).content
    with open('pfpimage.png', 'wb') as handler:
        handler.write(img_data)
    print(Fore.LIGHTGREEN_EX + "Uploading image to yandex.com")
    print(Fore.WHITE)
    filePath = "pfpimage.png"
    searchUrl = 'https://yandex.com/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json',
              'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = searchUrl + '?' + query_string
    print(Fore.LIGHTGREEN_EX + "Opening lookup.guru")
    print(Fore.WHITE)
    webbrowser.open(whole_url)
    print(Fore.LIGHTGREEN_EX + "Opening reverse image search result")
    webbrowser.open(img_search_url)
    print(Fore.WHITE + "\n")


userInput()
