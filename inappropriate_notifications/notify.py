"""Display innapropriate notifications at random intervals."""
import json
import random
from pathlib import Path
import subprocess
import time
import sys
from os import listdir, name as os_name

if os_name == 'nt':
    from win10toast import ToastNotifier
    ICON_FILETYPE = '.ico'
    TOASTER = ToastNotifier()
else:
    ICON_FILETYPE = '.jpg'

PROJECT_ROOT = Path(__file__).resolve().parent.parent
#TODO have different files for profession, age, location, etc
NOTIFICATION_PATH = PROJECT_ROOT / 'inappropriate_notifications' / 'notifications.json'
IMAGES_PATH       = PROJECT_ROOT / 'images'
ICONS_PATH        = PROJECT_ROOT / 'icons'


with NOTIFICATION_PATH.open('r', encoding="utf8") as notify_file:
    notifications = json.loads(notify_file.read())


def get_user(gender, string, get_icon=True):
    gendered_images_path = IMAGES_PATH / gender
    images = [x for x in gendered_images_path.iterdir() if x.suffix == ICON_FILETYPE]
    image = random.choice(images)
    string = string.replace(f"*{gender}", image.stem)
    if get_icon:
        return string, image
    return string

def notify_me():
    notification = random.choice(notifications)
    title = notification['title']
    escapables = ['!', '\'', '"', '$']
    content = notification['content'].replace("'", "\\\'").replace("\"", "\\\"")
        # https://xkcd.co/1638/
    
    icon = str((ICONS_PATH / notification['icon']))

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
        # print(f"title: {title}    icon: {icon}")
        subprocess.call(['notify-send', title, content, f"--icon={icon}", "--expire-time=10000"])

def run_random_notifications(seconds_between=10, number_notifications=100):
    time_range = list(range(int(0.5*seconds_between), 2*seconds_between)) or [0.1]

    for _ in range(number_notifications): 
        #TODO make this spawn a thread, and add another function to kill it
        time.sleep(random.choice(time_range))
        notify_me()

#TODO argparse
if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_random_notifications(int(sys.argv[1]))
    else:
        run_random_notifications()
