import requests
from tkinter import *
import math

city_name = 'Alajuela,CR'
api_key = 'a42bf8f1230c4eba7662de4ef60b0a37'

def get_weather(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = int(temp - 273.15)
    

    feels_like = response['main']['temp']
    feels_like = int(temp - 13.15)

    humidity = response['main']['humidity']

    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity       
    }

weather = get_weather(api_key, city_name)

print(weather['temp'])

root = Tk()
root.geometry('300x300')
root.title(f'{city_name[:-3]} Weather')

def display_city_name(city):
    city_label = Label(root, text=f"{city_name[:-3]}")
    city_label.config(font=('Consolas', 28))
    city_label.pack(side='top')

def display_stats(weather):
    temp = Label(root, text=f'Temperature: {weather["temp"]} C')
    feels_like = Label(root, text=f'Feels like: {weather["feels_like"]} C')
    humidity = Label(root, text=f'Humidity: {weather["humidity"]} %')

    temp.config(font=('Consolas', 22))
    feels_like.config(font=('Consolas', 16))
    humidity.config(font=('Consolas', 16))

    temp.pack(side='top')
    feels_like.pack(side='top')
    humidity.pack(side='top')


display_city_name(city_name) 
display_stats(weather)
mainloop()
