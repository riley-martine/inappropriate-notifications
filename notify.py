"""Display innapropriate notifications at random intervals."""
import json
import random
from pathlib import Path
import subprocess
from urllib.request import urlopen
import requests

with open("notifications.json") as notify_file:
    notifications = json.loads(notify_file.read())

notification = random.choice(notifications)
title = notification['title']
escapables = ['!', '\'', '"', '$']
content = notification['content'].replace("'", "\\\'").replace("\"", "\\\"")
icon = str((Path('icons') / notification['icon']).resolve())

for gender in ["female", "male"]: # in case they add the ability to get more
    if gender in title:
        r = urlopen(f"https://randomuser.me/api/?gender={gender}")
        j = json.loads(r.read().decode('utf-8'))
        name = j['results'][0]['name']['first'].title()
        title = title.replace(f"*{gender}", name)
    if gender in content:
        r = urlopen(f"https://randomuser.me/api/?gender={gender}")
        j = json.loads(r.read().decode('utf-8'))
        name = j['results'][0]['name']['first'].title()
        content = content.replace(f"*{gender}", name)
    if gender in icon:
        r = urlopen(f"https://randomuser.me/api/?gender={gender}")
        j = json.loads(r.read().decode('utf-8'))
        thumb = j['results'][0]['picture']['thumbnail']
        img_data = requests.get(thumb).content
        img = Path('images') / 'thumb.jpg'
        icon = str(img.resolve())
        print(thumb)
        with img.open('wb') as img_file:
            img_file.write(img_data)
        


subprocess.call(['notify-send', title, content, f"--icon={icon}"])
