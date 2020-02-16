Excel is a motivational type bot that posts a random quote to a designated slack channel at intervals

## Features

- **Scrapping tool** - Scrapes https://www.brainyquote.com/ and returns a list of quotes saved to a json file
- **Random quote generator** - Reads a JSON file and returns a random quote in a dictionary
- **Slack Bot** - Posts a message to a slack channel
- **Scheduler** - Runs the slack bot to send a message to a slack channel at different time intervals...

## Requirements and Installation

**Via Cloning The Repository**

```
# Make sure you have python installed
python --version

# Clone the app
git clone https://github.com/vic3king/excel.git

# Switch to directory
cd excel

# Create virtual env(make sure you have virtualenv installed)
virtualenv --python=python3 venv

# Activate virtual env
source venv/bin/activate

#  Create .env file and copy contents of .env.example and provide details
touch .env

# Install Package dependencies
pip3 install -r requirements.txt

#Start the application
- Run the scrapping tool: **python3 scrapping-tool/main.py**
- Run the app - **python3 app.py **

```

## Technologies

- [Python-Flask](http://flask.pocoo.org/) Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.
  
- [Selenium](https://selenium.dev/) - Selenium automates browsers. That's it!

- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - Beautiful Soup is a library that makes it easy to scrape information from web pages.

- [Slack API](https://pypi.org/project/slackclient/) - Slack API clients for Web API and RTM API.

- [APScheduler](https://jestjs.io/) - In-process task scheduler with Cron-like capabilities.

## Articles

- Coming soon
  
## Author

- **Akaniru victory** - _Initial work_ - [Vic3king](http://vic3king.io)
