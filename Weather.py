import requests
import json
import os

city = input("enter the name of city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=282a26fcb3f045549e8155307232104&q={city}"

r = requests.get(url)

print(r.text)
wdic = json.loads(r.text)
w=(wdic["current"]["temp_c"])

os.system(f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The current weather in {city} is {w}celcius')")

