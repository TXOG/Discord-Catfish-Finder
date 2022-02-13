import requests
import webbrowser
from selenium import webdriver
import time
import json
from selenium.webdriver.chrome.options import Options
from tkinter import *
import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


print("""            _____   _____ ______
           |  __ \ / ____|  ____|
           | |  | | |    | |__
           | |  | | |    |  __|
           | |__| | |____| |
           |_____/ \_____|_|

                       """)

global pfp
pfp = "a"
global needNewWindow
needNewWindow = 1


def guiScrapeResults():
    global window
    global whole_url
    window.destroy()
    img_data = requests.get(pfp).content
    with open('pfpimage.png', 'wb') as handler:
        handler.write(img_data)
    filePath = "pfpimage.png"
    searchUrl = 'https://yandex.com/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json',
              'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = searchUrl + '?' + query_string
    webbrowser.open(whole_url)
    webbrowser.open(img_search_url)


def guiScrape():
    global window
    global entry
    global pfp
    global target_id
    global textbox
    global needNewWindow
    global userName
    global whole_url
    try:
        target_id = entry.get()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        begining_of_url = "https://lookup.guru/"
        whole_url = begining_of_url + str(target_id)
        driver.get(whole_url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img")))
        images = driver.find_elements_by_tag_name('img')
        for image in images:
            global pfp
            pfp = (image.get_attribute('src'))
            break
        if pfp == "a":
            textbox.delete('1.0', END)
            textbox.insert(END, "User not found")
            needNewWindow = 0
            guiUserInput()
        else:
            textbox.delete('1.0', END)
            textbox.insert(END, "User found")
            userFoundButton = Button(
                window, width=15, text="Click to search", command=guiScrapeResults)
            userFoundButton.grid(row=4, column=0, sticky=E)
        window.mainloop()
    except:
        textbox.delete('1.0', END)
        textbox.insert(END, "User not found")
        window.mainloop()


def guiUserInput():
    global window
    global entry
    global textbox
    global needNewWindow
    if needNewWindow == 1:
        window = Tk()
        window.title("DCF")
        enterIdLable = Label(window, text="Enter target ID:")
        enterIdLable.grid(row=0, column=0, sticky=W)
        entry = Entry(window, width="20", bg="light green")
        entry.grid(row=1, column=0, sticky=W)
        spaceLabel1 = Label(window, text="")
        spaceLabel1.grid(row=2, column=0, sticky=N)
        scrapeButton = Button(window, width=5, text="GO", command=guiScrape)
        scrapeButton.place(x=80, y=40)
        textbox = Text(window, width=85, height=20,
                       wrap=WORD, background="yellow")
        textbox.grid(row=3, column=0, sticky=S)
        textbox.insert(
            END, "Depending on wifi speed, the program may take a while to load results. Ignore any messages saying the program is not responding")
        window.mainloop()
    window.mainloop()


guiUserInput()
