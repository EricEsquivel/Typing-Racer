import random
import requests
from bs4 import BeautifulSoup
import time


def text_appender(): #searches through type racer database for text and adds it to text_file if found
    current = 5390433
    max_tries = 500
    for attempt in range(current, current+max_tries):
        random_text = str(attempt)
        website = (f"https://data.typeracer.com/pit/text_info?id={random_text}")
        # request to typeracer website for random text
        response = requests.get(website).text
        print(website)
        # parse information to get text
        try:
            parsed_text = BeautifulSoup(response, features="html.parser")
            text_to_type = parsed_text.find('div', class_="fullTextStr").text
            with open("text_file", "a") as text_file:
                text_file.write(text_to_type + "\n")
        except AttributeError:
            print(f"No text found at website: {website}")
        time.sleep(10)
    print(f"Ended at: {random_text}")


def call_available_text(): #open file and pick a random line of text to use in type racer
    open_text_file = open("text_file").read().splitlines()
    randomline = random.choice(open_text_file)
    return randomline

if __name__ == "__main__":
    text_appender()
    #call_available_text()