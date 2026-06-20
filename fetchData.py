import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import json

main_directory = "Saved_Articles"

if not os.path.exists(main_directory):
    os.makedirs(main_directory, exist_ok=True)

load_dotenv()
api = os.getenv('API')

url = "https://content.guardianapis.com/technology/artificialintelligenceai?&api-key=" + api + "&type=article&page=1"

response = requests.get(url)
x = response.json()

web_urls = [item['webUrl'] for item in x['response']['results']][5:7]


def save_content_to_file(url, folder, filename):
    try:
        response = requests.get(url)

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


for index, url in enumerate(web_urls):
    filename = f'article_{index}.json'
    save_content_to_file(url, main_directory, filename)