"""Pull num_pull male and num_pull female profiles from randomuser.me"""
import json
from pathlib import Path
from urllib.request import urlopen
from os import listdir
import requests

num_pull = 100


def download_user(gender, get_icon=True):
    """Get a username and icon to go with it, unless it's already been saved"""
    r = urlopen(f"https://randomuser.me/api/?gender={gender}")
    j = json.loads(r.read().decode("utf-8"))
    name = j["results"][0]["name"]["first"].title()

    if get_icon:
        thumb = j["results"][0]["picture"]["thumbnail"]
        img_data = requests.get(thumb).content
        if gender == "female":
            icons = listdir("images/female/")
            if name + ".jpg" in icons:
                return "Profile already downloaded, passing", "NULL"
            img = Path("images/female/%s.jpg" % name)
        elif gender == "male":
            icons = listdir("images/male/")
            if name + ".jpg" in icons:
                return "Profile already downloaded, passing", "NULL"
            img = Path("images/male/%s.jpg" % name)
        else:
            img = Path("images/%s.jpg" % name)
        icon = str(img.resolve())
        with img.open("wb") as img_file:
            img_file.write(img_data)

    return name, icon


for gender in ["female", "male"]:
    for run in range(0, num_pull):
        user = download_user(gender)
        print(run, user[0], user[1])
