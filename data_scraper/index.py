from bs4 import BeautifulSoup
import requests
import csv

URL="https://www.buzzfeed.com/williambarrios/best-star-wars-quotes"
page = requests.get(URL)

# print(page)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="buzz-content")

# print(results.prettify())

quotes = results.find_all("span", class_="js-subbuzz__title-text")

quotes = [q for q in quotes if (("Star Wars" not in q.text) and ("(" not in q.text))]

quotes = quotes[1:]

# print(quotes)

all_quotes = []

for q in quotes: 
    # print(q.text)
    quote = {}
    parts = q.text.split(': ')
    print(parts[1].replace('"', ''))
    quote['character'] = parts[0]
    quote['quote'] = parts[1].replace('"', '')
    # print(quote)
    all_quotes.append(quote)

# print(all_quotes)

csv_file = "sw_quotes.csv"

# Extract the fieldnames (column headers) from the key-value pairs in the dictionaries
fieldnames = all_quotes[0].keys()
print(fieldnames)

with open(csv_file, mode='w', newline='') as file:
    # Create a CSV writer
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    for row in all_quotes:
        writer.writerow(row)