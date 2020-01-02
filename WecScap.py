import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.XgvmUCHVLDc")
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast-body')
items= week.find_all(class_='tombstone-container')
#print(items[0])

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names =[item.find(class_= 'period-name').get_text() for item in items]
short_description =[item.find(class_= 'short-desc').get_text() for item in items]
temperature =[item.find(class_= 'temp.temp-high').get_text() for item in items]

#print(period_names)
#print(short_description )
print(temperature)

weather_stuff = pd.DataFrame({
    'periof' :period_names,
    'short_decsription' : short_description,
    'temperature' : temperature
})
print(weather_stuff)

weather_stuff.to_csv('weather.csv')


