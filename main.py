from bs4 import BeautifulSoup
import requests


#add search varible
search = input("Enter search Term:")
#add parameter variable
params = {"q": search}
r = requests.get("https://www.bing.com/images/search",params=params)

soup = BeautifulSoup(r.text,"html.parser")
results = soup.find("ol",{"id":"b_results"})
links = results.findAll("li",{"class":"b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)