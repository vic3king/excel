import random
import json

def random_quotes_generator():
    with open('quotes.json', 'r') as f:
        quotes_dict = json.load(f)
  
    res = key, val = random.choice(list(quotes_dict.items()))
    print(res)

random_quotes_generator()