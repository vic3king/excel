import random
import json


def random_quotes_generator():
    with open('quotes.json', 'r') as f:
        quotes_dict = json.load(f)


        res = random.choice(quotes_dict)
        return res

