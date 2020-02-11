import re
import json
from bs4 import BeautifulSoup
from selenium_driver import driver
from scroll import scroll

def get_quotes(url):
    try:
        # implicitly_wait tells the driver to wait before throwing an exception
        driver.implicitly_wait(30)
        # driver.get(url) opens the page
        driver.get(url)
        # This starts the scrolling by passing the driver and a timeout
        scroll(driver, 5)
        # Once scroll returns bs4 parsers the page_source
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Them we close the driver as soup_a is storing the page source
        driver.close()

        # Empty array to store the links
        quotes = []

        regex = re.compile('^b-qt')
        quotes_list = soup.find_all('a', attrs={'class': regex})
        # Looping through all the a elements in the page source
        for quote in quotes_list:
            quotes.append({
                "text": quote.get_text()
            })

            with open("quotes.json", 'w') as json_file:
                json.dump(quotes, json_file)
    except Exception as e:
        print(e, '>>>>>>>>>>>>>>>Exception>>>>>>>>>>>>>>')

get_quotes('https://www.brainyquote.com/topics/excellence-quotes')