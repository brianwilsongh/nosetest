
import logging
import requests
import utils
import collections
import csv

# Using the Star Wars API (https://swapi.co/)
# 
# TODO: 1. Find the ten characters who appear in the most Star Wars films
# TODO: 2. Sort those ten characters by height in descending order (i.e., tallest first)
# TODO: 3. Produce a CSV with the following columns: name, species, height, appearances
# TODO: 4. Send the CSV to httpbin.org
# TODO: 5. Create automated tests that validate your code

BASE_URL = "http://swapi.co/api/"
PASTEBIN = "http://httpbin.org/post"
DEFAULT_FILENAME = "file.csv"

def main():
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S', level=logging.DEBUG)
    # logging.getLogger().setLevel(logging.DEBUG)
    # logging.Formatter('')
    people = utils.get_all(BASE_URL+"people")
    people.sort(key=lambda x: len(x['films']), reverse=True)
    people = people[:9]
    people.sort(key=lambda x: int(x['height']), reverse=True)
    with open(DEFAULT_FILENAME, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["name", "species", "height", "appearances"])
        for char in people:
            writer.writerow([char['name'], utils.get_one(char['species'][0])['name'], char['height'], len(char['films'])])
    upload_status = utils.send_file_to_url(PASTEBIN, DEFAULT_FILENAME)
    if upload_status:
        print("File uploaded successfully!")
    else:
        print("File upload unsuccessful...")


if __name__ == "__main__":
    main()