

import requests
from dotenv import load_dotenv
load_dotenv()
import os


url="https://api.nasa.gov/planetary/apod?api_key="
unique_key=os.getenv("NASA_API_KEY")

final_url = url + unique_key

def apod_generator(url, unique_key):
    final_url =  url + unique_key
    response = requests.get(final_url).json()
    return response



