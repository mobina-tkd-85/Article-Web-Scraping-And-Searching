import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import json
import re
from datetime import datetime

main_directory = "Saved_Articles"

sections = ['football', 'sport']


if not os.path.exists(main_directory):
    os.makedirs(main_directory, exist_ok=True)

load_dotenv()
api = os.getenv('API')

all_urls = []


for section in sections :
    for i in range(1,5):
        url = "https://content.guardianapis.com/"+ section +"?&api-key=" + api + "&type=article&page=" + str(i)
        response = requests.get(url)
        x = response.json()
        web_urls = [(item['webUrl'], section) for item in x['response']['results']]
        all_urls += web_urls




def extract_guardian_date(url):
    match = re.search(r'/(\d{4})/([a-z]{3})/(\d{1,2})/', url.lower())
    
    if not match:
        return None

    year, month_str, day = match.groups()

    month_map = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4,
        "may": 5, "jun": 6, "jul": 7, "aug": 8,
        "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    return datetime(int(year), month_map[month_str], int(day)).date()


def save_content_to_file(url, folder, filename):
    section = url[1]
    url = url[0]
    try:
        response = requests.get(url)
        date = extract_guardian_date(url)
        date = str(date)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            title = None
            for h1 in soup.find_all('h1'):
                title = h1.text.strip()

            paragraphs = []
            for p in soup.find_all('p'):
                text = p.text.strip()
                if text:
                    paragraphs.append(text)

            article_data = {
                "section": section,
                "date": date,
                "url": url,
                "title": title,
                "paragraphs": paragraphs
            }

            file_path = os.path.join(folder, filename)

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(article_data, file, ensure_ascii=False, indent=4)

        else:
            print("Failed to retrieve the page:", url)

    except Exception as e:
        print("An error occurred:", e)


for index, url in enumerate(all_urls):
    filename = f'article_{index}.json'
    save_content_to_file(url, main_directory, filename)