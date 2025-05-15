import requests
from bs4 import BeautifulSoup
import csv
import time

def get_animals_count():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    letter_counts = {}

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        content_div = soup.find('div', id='mw-pages')
        if not content_div:
            break

        category_groups = content_div.find_all('div', class_='mw-category-group')

        for group in category_groups:
            links = group.find_all('a')
            for link in links:
                title = link.text.strip()
                if title:
                    first_letter = title[0].upper()
                    letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1

        next_page = soup.find('a', string='Следующая страница')
        if not next_page:
            break

        print(letter_counts)
        print(url)
        url = "https://ru.wikipedia.org" + next_page['href']
        time.sleep(0.3)

    return letter_counts

def save_to_csv(letter_counts, filename='beasts.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(letter_counts.keys()):
            writer.writerow([letter, str(letter_counts[letter])])

if __name__ == '__main__':
    counts = get_animals_count()
    save_to_csv(counts)
