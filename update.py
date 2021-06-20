import requests
import base64
import time
import shutil
import os
from datetime import datetime
import glob
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")

def update_scrapper():
    token = str(base64.b64decode("OGZiNDVkOGMzZGJhODc5NTUyN2NmYjRjNDM3NjAyMWQxZWYwZDcxMA==").decode("utf-8"))
    headers = {'Authorization': 'token ' + token}
    res = requests.get("https://raw.githubusercontent.com/aashishsaini75/blog_generator/master/blog_generator.py",headers = headers)
    if res.status_code ==200:
        with open("blog_generator.py",'w',encoding="utf-8") as file:
            file.write(res.text)
            file.close()
        print("Scrapper updated successfully")
        time.sleep(3)
    else:
        print(str(res.status_code)+" Error, Suit not updated, Please contact to aashish@shorthillstech.com")
        time.sleep(10)
    res = requests.get("https://raw.githubusercontent.com/aashishsaini75/blog_generator/master/requirement.txt",headers=headers)
    if res.status_code == 200:
        with open("requirements.txt", 'w', encoding="utf-8") as file:
            file.write(res.text)
            file.close()
        print("requirements.txt updated successfully")
        time.sleep(3)
    else:
        print(str(res.status_code) + " Error, Suit not updated, Please contact to aashish@shorthillstech.com")
        time.sleep(10)
update_scrapper()