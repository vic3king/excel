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
        soup = BeautifulSoup(driver.page_source, "lxml")
        # Them we close the driver as soup_a is storing the page source
        driver.close()

        # Empty array to store the links
        quotes = []

        regex_quotes = re.compile('^b-qt')
        regex_authors = re.compile('^bq-aut')

        quotes_list = soup.find_all('a', attrs={'class': regex_quotes})
        authors_list = soup.find_all('a', attrs={'class': regex_authors})

        quotes = []
        zipped_quotes = list(zip(quotes_list, authors_list))
        for i, x in enumerate(zipped_quotes):
            quote = x[0]
            author = x[1]
            quotes.append({
                "id":  f"id-{i}",
                "quote": quote.get_text(),
                "author": author.get_text(),
                "author-link": author.get('href')
            })

        with open("quotes.json", 'w') as json_file:
            json.dump(quotes, json_file)
    except Exception as e:
        print(e, '>>>>>>>>>>>>>>>Exception>>>>>>>>>>>>>>')


get_quotes('https://www.brainyquote.com/topics/excellence-quotes')
