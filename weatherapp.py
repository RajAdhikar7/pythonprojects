
import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


city  = input ("Enter the name of the city \n")

url = f"http://api.weatherapi.com/v1/current.json?key=74225de09bf14ea182c70448233010&q={city}&aqi=no"

r = requests.get(url)

wdic = json.loads(r.text)

w = wdic["current"]["temp_c"]

speaker.Speak(f"the current weather in {city} is {w} degree celcius")
