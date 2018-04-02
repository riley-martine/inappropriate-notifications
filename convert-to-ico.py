"""Pull all profile pictures from randomuser.me and save them to images in .ico format. Also make sure copies of all images in icons/ exist in .ico format."""
from io import BytesIO
from os import path, listdir
from PIL import Image
import requests

pull_icons = False
convert_images = True
convert_icons = True

num_icons = 99
url = 'https://randomuser.me/api/portraits/thumb/'
gendered_urls = ['women/', 'men/']
gendered_paths = ['female/', 'male/']

if pull_icons:
    for gender in gendered_urls:
        for icon in range(1, num_icons + 1):
            print(gender, icon)
            if not path.exists('images/%s%d.ico' %(gender, int(icon))):
                response = requests.get(url + gender + str(icon) + '.jpg')
                img = Image.open(BytesIO(response.content))
                # https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python
                img.save('images/%s%d.ico' %(gender, int(icon)))

if convert_images:
    print('converting images...')
    for gender in gendered_paths:
        icons = listdir('images/' + gender)
        for icon in icons:
            if not path.exists('images/%s%s.ico' %(gender, icon[:-3])):
                copy = Image.open('images/%s%s' %(gender, icon))
                path = 'images/' + gender + icon[:-3] + 'ico'
                print(path)
                copy.save(path)

if convert_icons:
    print('converting icons...')
    icons = listdir('icons/')
    for img in icons:
        if img[len(img) - 3:] != 'ico':
            if not path.exists('icons/%sico' %img[:-4]):
                copy = Image.open('icons/' + img)
                path = 'icons/' + img[:len(img) - 3] + 'ico'
                print(path)
                copy.save(path)