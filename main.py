import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the city")
    raise SystemExit(2)

city = sys.argv[1]
#call the weather api using the city 

# Path: weather.py
import requests
import json, os
from dotenv import load_dotenv
load_dotenv()

url= f'http://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={os.getenv("APPID")}'
r=requests.get(url)
data=r.json()
print(data)


    
