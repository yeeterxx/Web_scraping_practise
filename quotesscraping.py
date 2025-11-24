from bs4 import BeautifulSoup
import requests
import json


all_quotes=[]



for page in range(1,6):
    url= f"https://quotes.toscrape.com/page/{page}"
    source= requests.get(url)

    soup=BeautifulSoup(source.text, "lxml")

    quotes= soup.find_all("div", class_="quote")
    

    for quote in quotes:
        main_quote= quote.find("span", class_="text").text
        
        author= quote.find("small", class_="author" ).text
        
        tags= quote.find("meta", class_="keywords")['content'].split(',')
        print(tags)

        all_quotes.append({"quote":main_quote, "author":author, "tags":tags})
        print(all_quotes)
        print()

with open("quotes.json",'w') as f:
    json.dump(all_quotes, f, indent=4)