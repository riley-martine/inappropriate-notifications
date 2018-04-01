"""Display innapropriate notifications at random intervals."""
import json
import random
from pathlib import Path
import subprocess
from urllib.request import urlopen
import requests # do we use requests and urllib? yes, yes we do.
import time
import sys
from os import listdir, name
from win10toast import ToastNotifier

with open("notifications.json", encoding="utf8") as notify_file:
    notifications = json.loads(notify_file.read())


def get_user(gender, string, get_icon=True):
    """Get a username and icon to go with it, replace gender in string."""
    # no check becuase this is cheap
    r = urlopen(f"https://randomuser.me/api/?gender={gender}")
    j = json.loads(r.read().decode('utf-8'))
    name = j['results'][0]['name']['first'].title()
    string = string.replace(f"*{gender}", name)
    
    if get_icon:
        thumb = j['results'][0]['picture']['thumbnail']
        img_data = requests.get(thumb).content
        img = Path('images') / 'thumb.jpg'
        icon = str(img.resolve())
        with img.open('wb') as img_file:
            img_file.write(img_data)
    
        return string, icon
    return string


def notify_me():
    notification = random.choice(notifications)
    title = notification['title']
    escapables = ['!', '\'', '"', '$']
    content = notification['content'].replace("'", "\\\'").replace("\"", "\\\"")
        # https://xkcd.co/1638/
    if name == 'nt':
        icon = 'icons/%s' %notification['icon']
    else:
        icon = str((Path('icons') / notification['icon']).resolve())
    
    for gender in ["female", "male"]: # in case they add the ability to get more
        # put "female" first because "male" is within female
        if gender in title and icon in title:
            title, icon = get_user(gender, title)
            print(icon)
        elif gender in title:
            title = get_user(gender, title, get_icon=False)
         
        if gender in content:
            content = get_user(gender, content, get_icon=False)

        if gender in icon:
           tmp, icon = get_user(gender, "")
           print(icon)
    
    if name == 'nt':
        print(icon)
        if 'thumb' in icon:
            if 'female' in title:
                icon = 'images/women/' + random.choice(listdir('images/women/'))
            else:
                icon = 'images/men/' + random.choice(listdir('images/men/'))
        else:
            icon = icon[:len(icon) - 3] + 'ico'
        toaster = ToastNotifier()
        toaster.show_toast(title, content, icon_path=icon, duration=10)
    else:
        # Used w/o shell=True so that escaping works
        subprocess.call(['notify-send', title, content, f"--icon={icon}"])

if __name__ == "__main__":
    time_between = 10 # in seconds
    if len(sys.argv) > 1:
        time_between = int(sys.argv[1])

    time_range = list(range(int(0.5*time_between), 2*time_between))
    
    while True:
        time.sleep(random.choice(time_range))
        notify_me()
