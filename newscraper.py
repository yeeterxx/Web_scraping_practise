from bs4 import BeautifulSoup
import requests
import json

url="https://www.onlinekhabar.com/"
source= requests.get(url)
source.encoding="utf-8"
soup= BeautifulSoup(source.text, "lxml")

news_titles= soup.find_all("div", class_="ok-news-post ok-post-ltr")
all_news=[]

seen_links= set()


for news in news_titles:
    
    title_tag= news.find("h2", class_="ok-news-title-txt")
    title= title_tag.text.strip() if title_tag else "Title not found"

    link_tag= news.find("a")
    links= link_tag["href"] if link_tag else "link not found"
    
    time_tag= news.find("div", class_="ok-news-post-hour")
    time= time_tag.find("span").text.strip() if time_tag else "time not found"

    if links not in seen_links:
     
        page= requests.get(links)
        page.encoding = 'utf-8'
        article= BeautifulSoup(page.text, "lxml")

        paragraphs = [p.text.strip() for p in article.find_all("p")]

        all_news.append({"title":title, "links":links, "time": time, "content":"\n\n".join(paragraphs)})
        seen_links.add(links)

for new_news in all_news:
   print("Title:", new_news['title'])
   print("links:", new_news['links'])
   print("time:", new_news['time'])
   print("content:", new_news['content'][:500])
   print("-"*50)

with open("news.json", 'w') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)

     
     



