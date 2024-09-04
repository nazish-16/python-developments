import requests
import json
import pyttsx3

city = input("Enter the name of your city:\n")
url = f"http://api.weatherapi.com/v1/current.json?key=c195755095b84a61b8991204240409&q={city}"
engine = pyttsx3.init()

r = requests.get(url)
weatherDict = json.loads(r.text)
temp = weatherDict["current"]["temp_c"]
print(f"The weather in {city} is {temp}°C")
engine.say(f"The weather in {city} is {temp}°C")
engine.runAndWait()