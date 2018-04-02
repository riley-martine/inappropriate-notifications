"""Display innapropriate notifications at random intervals."""
import json
import random
from pathlib import Path
import subprocess
from urllib.request import urlopen
import requests # do we use requests and urllib? yes, yes we do.
import time
import sys
from os import listdir, name as os_name

if os_name == 'nt':
    from win10toast import ToastNotifier
    ICON_FILETYPE = 'ico'
    TOASTER = ToastNotifier()
else:
    ICON_FILETYPE = 'jpg'

with open("notifications.json", encoding="utf8") as notify_file:
    notifications = json.loads(notify_file.read())


def get_user(gender, string, get_icon=True):
    icons = list(filter(lambda x: x.endswith(ICON_FILETYPE), listdir('images/' + gender)))
    icon = random.choice(icons)
    name = icon[:-4]
    icon = (Path('./images') / gender / icon).resolve()
    string = string.replace(f"*{gender}", name)
    if get_icon:
        return string, icon
    return string

def notify_me():
    notification = random.choice(notifications)
    title = notification['title']
    escapables = ['!', '\'', '"', '$']
    content = notification['content'].replace("'", "\\\'").replace("\"", "\\\"")
        # https://xkcd.co/1638/
    if os_name == 'nt':
        icon = 'icons/%sico' %notification['icon'][:-3]
    else:
        icon = str((Path('icons') / notification['icon']).resolve())
    
    if '*female' in title or '*female' in icon:
        title, icon = get_user('female', title)
    elif '*male' in title or '*male' in icon:
        title, icon = get_user('male', title)
    
    if '*female' in content:
        content = get_user('female', content, get_icon=False)
    elif '*male' in content:
        content = get_user('male', content, get_icon=False)

    if os_name == 'nt':
        TOASTER.show_toast(title, content, icon_path=icon, duration=10)
    else:
        # Used w/o shell=True so that escaping works
        #print(f"title: {title}    icon: {icon}")
        subprocess.call(['notify-send', title, content, f"--icon={icon}"])

if __name__ == "__main__":
    time_between = 10 # in seconds
    if len(sys.argv) > 1:
        time_between = int(sys.argv[1])

    time_range = list(range(int(0.5*time_between), 2*time_between)) or [0.1]
    print(time_range)
    

    while True:
        time.sleep(random.choice(time_range))
        notify_me()
