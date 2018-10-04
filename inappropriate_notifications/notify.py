"""Display innapropriate notifications at random intervals."""
import json
import random
import subprocess
import sys
import time
from os import name as os_name
from pathlib import Path

if os_name == "nt":
    from win10toast import ToastNotifier

    ICON_FILETYPE = ".ico"
    TOASTER = ToastNotifier()
else:
    ICON_FILETYPE = ".jpg"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# TODO have different files for profession, age, location, etc
NOTIF_PATH = PROJECT_ROOT / "inappropriate_notifications" / "notifications.json"
IMAGE_PATH = PROJECT_ROOT / "inappropriate_notifications" / "images"
ICONS_PATH = PROJECT_ROOT / "inappropriate_notifications" / "icons"
ICON = lambda name: str(ICONS_PATH / name)

with NOTIF_PATH.open("r", encoding="utf8") as notify_file:
    NOTIFICATIONS = json.loads(notify_file.read())


def get_user(gender, string, get_icon=True):
    """Get a user with specified gender, substitute their name into a string,
    and optionally return icon."""
    gendered_images_path = IMAGE_PATH / gender
    images = [x for x in gendered_images_path.iterdir() if x.suffix == ICON_FILETYPE]
    image = random.choice(images)
    string = string.replace(f"*{gender}", image.stem)
    if get_icon:
        return string, image
    return string


def get_icon(icon_name):
    """Locate icon file or default icon name, depending on platform."""
    icon_files = {
        "calendar": "cal.ico",
        "mail": "mail.png",
        "messenger": "imessage.png",
        "grindr": "grindr.png",
        "facebook": "facebook.png",
        "slack": "slack.png",
        # The user-icon getting code is reached later
        # I'm doing it this way so images match up with names.
        "*female": "*female",
        "*male": "*male",
    }
    icon_default_names = {
        # Is this cross platform enough or does it depend on having a certain icon
        #    pack installed?
        "calendar": "gnome-calendar",
        "mail": "gmail",  # Note: using google/fb icons because of recognizability
        "messenger": "fbmessenger",
        "grindr": ICON("grindr.png"),
        "facebook": "facebook",
        "slack": "slack",
        "*female": "*female",
        "*male": "*male",
    }
    if os_name == "nt":
        return ICON(icon_files[icon_name])  # Perhaps better error handling?
    # linux
    return icon_default_names[icon_name]


def notify_me():
    """Generate a random notification and display it onscreen."""
    notification = random.choice(NOTIFICATIONS)
    title = notification["title"]
    # escapables = ['!', '\'', '"', '$']
    content = notification["content"].replace("'", "\\'").replace('"', '\\"')
    # https://xkcd.com/1638/

    icon = get_icon(notification["icon"])

    if "*female" in title or "*female" in icon:
        title, icon = get_user("female", title)
    elif "*male" in title or "*male" in icon:
        title, icon = get_user("male", title)

    if "*female" in content:
        content = get_user("female", content, get_icon=False)
    elif "*male" in content:
        content = get_user("male", content, get_icon=False)

    if os_name == "nt":
        TOASTER.show_toast(title, content, icon_path=icon, duration=10)
    else:
        # Used w/o shell=True so that escaping works
        # print(f"title: {title}    icon: {icon}")
        subprocess.call(
            ["notify-send", title, content, f"--icon={icon}", "--expire-time=10000"]
        )


def run_random_notifications(seconds_between=10, number_notifications=100):
    """Create random notifications and display them, at random intervals."""
    time_range = list(range(int(0.5 * seconds_between), 2 * seconds_between)) or [0.1]

    for _ in range(number_notifications):
        # TODO make this spawn a thread, and add another function to kill it
        time.sleep(random.choice(time_range))
        notify_me()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_random_notifications(int(sys.argv[1]))
    else:
        run_random_notifications()
