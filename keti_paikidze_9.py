'''
ვებსაიტზე http://quotes.toscrape.com/author/Albert-Einstein/ განთავსებულია
ინფორმაცია ერთ-ერთი ცნობილი მეცნიერის შესახებ. ამოიკითხეთ ამ
მეცნიერის სახელი, დაბადების თარიღი და აღწერილობა. ამოკითხული
ინფორმაცია ჩაწერეთ JSON ფაილში.
'''
import json
from typing import List
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
import requests

URL = requests.get("http://quotes.toscrape.com/author/Albert-Einstein/").text

bs: BeautifulSoup = BeautifulSoup(URL, 'html.parser')

author_details: List[Tag] = bs.find(attrs={"class": "author-details"})
data = []
for details in author_details:
    name :List[Tag] = details.find(attrs={'class': "author-title"})
    born_date :List[Tag] = details.find(attrs={'class': "author-born-date"})
    author_description :List[Tag] = details.find(attrs={'class': "author-description"})
    details = {
        'name' : name,
        'born-date' : born_date,
        'author-description': author_description

    }
    data.append(details)

with open('details.json', 'w') as f:
    json.dump(data, fp=f)


