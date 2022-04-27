#guaranteed imports
import os
import json
#pip imports
try:
    import requests
    import webbrowser
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from rich.console import Console
    from rich.theme import Theme
    from rich.progress import Progress
except:
    try:
        os.system("pipinstalls.bat")
    except Exception as e:
        print(e)
        print("\nWe don't know what happened, please create an issue on the github with the error message above")
        userpause = input()
        exit()
print(""" _____   _____ ______
|  __ \ / ____|  ____|
| |  | | |    | |__
| |  | | |    |  __|
| |__| | |____| |
|_____/ \_____|_|
                       """)


global pfp
pfp = "a"


def userInput():
    theme = Theme({'success': 'bold green',
                  'error': 'bold red', 'enter': 'bold blue'})
    console = Console(theme=(theme))
    while True:
        global target_id
        try:
            console.print("\n")
            console.print("Enter target id: ", style='enter')
            target_id = int(input())
            scraping()
        except ValueError:
            console.print("Target id needs to be an integer \n", style='error')


def scraping():
    theme = Theme({'success': 'bold green',
                  'error': 'bold red', 'enter': 'bold blue'})
    console = Console(theme=(theme))
    bartotal = 100

    with Progress() as progress:
        task1 = progress.add_task("[magenta bold]Scraping...", total=bartotal)
        try:
            while not progress.finished:
                global pfp
                progress.update(task1, advance=4, description=(
                    "[green bold]Declaring global variables"))
                global target_id
                progress.update(task1, advance=4)
                chrome_options = Options()
                progress.update(task1, advance=4, description=(
                    "[green bold]Setting up chrome driver"))
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--log-level=3")
                progress.update(task1, advance=4)
                driver = webdriver.Chrome(options=chrome_options)
                progress.update(task1, advance=4, description=(
                    "[green bold]Creating url for lookup.guru"))
                begining_of_url = "https://lookup.guru/"
                progress.update(task1, advance=4)
                whole_url = begining_of_url + str(target_id)
                progress.update(task1, advance=4)
                driver.get(whole_url)
                progress.update(task1, advance=4)
                console.print(
                    "\nWaiting up to 10 seconds for lookup.guru to load", style='success')
                wait = WebDriverWait(driver, 10)
                progress.update(task1, advance=4,
                                description=("[green bold]Scraping images"))
                wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//img")))
                progress.update(task1, advance=4)
                images = driver.find_elements_by_tag_name('img')
                progress.update(task1, advance=4)
                for image in images:
                    global pfp
                    pfp = (image.get_attribute('src'))
                    break
                progress.update(task1, advance=4)
                if pfp == "a":
                    console.print("User not found \n", style='error')
                    userInput()
                progress.update(task1, advance=4, description=(
                    "[green bold]Downloading image to current directory"))
                img_data = requests.get(pfp).content
                progress.update(task1, advance=4)
                with open('pfpimage.png', 'wb') as handler:
                    handler.write(img_data)
                progress.update(task1, advance=4)
                filePath = "pfpimage.png"
                progress.update(task1, advance=4, description=(
                    "[green bold]Uploading to yandex.com"))
                searchUrl = 'https://yandex.com/images/search'
                progress.update(task1, advance=4)
                files = {'upfile': ('blob', open(
                    filePath, 'rb'), 'image/jpeg')}
                progress.update(task1, advance=4)
                params = {'rpt': 'imageview', 'format': 'json',
                          'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
                progress.update(task1, advance=4)
                response = requests.post(searchUrl, params=params, files=files)
                progress.update(task1, advance=4)
                query_string = json.loads(response.content)[
                                          'blocks'][0]['params']['url']
                progress.update(task1, advance=4)
                img_search_url = searchUrl + '?' + query_string
                progress.update(task1, advance=4, description=(
                    "[green bold]Opening lookup.guru"))
                webbrowser.open(whole_url)
                progress.update(task1, advance=4, description=(
                    "[green bold]Opening yandex.com"))
                webbrowser.open(img_search_url)
                progress.update(task1, advance=4)
                progress.update(task1, advance=4,
                                description=("[green bold]Done!"))
        except Exception as e:
            console.print("\n")
            console.print(e, style='error')
            console.print("\nThe process terminated due to an error (as shown above) - You can try: \nDouble checking the id \nChecking your internet connection \nChecking if lookup.guru and yandex.com are up \nUpdating your chrome driver (more details in github readme.md)", style='error')
            console.print(
                "\nPlease create an issue on the github with your error message so if there is an issue we can fix it :)", style='error')


userInput()
