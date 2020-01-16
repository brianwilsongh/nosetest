
import logging

BASE_URL = "http://swapi.co/api/"
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

def main():
    people = utils.get_all(BASE_URL+"people")
    people.sort(key=lambda x: len(x['films']), reverse=True)
    people = people[:9]
    people.sort(key=lambda x: int(x['height']), reverse=True)
    for person in people:
        print(person['height'])
    with open('chars.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["name", "species", "height", "appearances"])
        for char in people:
            writer.writerow([char['name'], utils.get_one(char['species'][0])['name'], char['height'], len(char['films'])])
    



if __name__ == "__main__":
    main()