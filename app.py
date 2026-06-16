import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

current_datetime = datetime.now()
folder_name = current_datetime.strftime('%H_%M_%d_%m_%Y')  # Format the current date and time for directory name

# Define the main directory to save articles
main_directory = "Saved_Articles"

# Create the main directory if it doesn't exist
if not os.path.exists(main_directory):
    os.makedirs(main_directory, exist_ok=True)

# Create a subdirectory with the current date and time format inside the main directory
subdirectory_path = os.path.join(main_directory, folder_name)
if not os.path.exists(subdirectory_path):
    os.makedirs(subdirectory_path, exist_ok=True)

# Define the URL to fetch data
load_dotenv()
api = os.getenv('API')
url = "https://content.guardianapis.com/technology/artificialintelligenceai?&api-key="+ api + "&type=article&page=1"

response = requests.get(url)  # Fetch data from the URL
x = response.json()  # Convert the response to JSON format

web_urls = [item['webUrl'] for item in x['response']['results']][5:7]

def save_content_to_file(url, folder, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            with open(os.path.join(folder, filename), 'w', encoding='utf-8') as file:
                for header in soup.find_all(['h1']):
                    file.write("Title: " + header.text + '\n' * 5)
                for paragraph in soup.find_all('p'):
                    file.write(paragraph.text + '\n')
        else:
            print("Failed to retrieve the page:", url)
    except Exception as e:
        print("An error occurred:", e)

for index, url in enumerate(web_urls):
    filename = f'article_{index}.txt'  # Create a unique filename for each article
    save_content_to_file(url, subdirectory_path, filename)  # Save the content to a file in the subdirectory