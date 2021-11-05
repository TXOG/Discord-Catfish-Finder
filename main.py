import requests
from bs4 import BeautifulSoup
import webbrowser
import re


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
    page = requests.get(whole_url)
    parsepage = BeautifulSoup(page.content, 'html.parser')
    links = parsepage.find_all('a', attrs={'href': re.compile("^https://")})
    print(links)
    #### ^

    string1 = ("discordapp.com")

    flag = 0
    index = 0

    # Loop through the file line by line
    for line in links:
        index += 1

        # checking string is present in line or not
        if string1 in line:
            #print
          flag = 1
          break


target_id_enter()
