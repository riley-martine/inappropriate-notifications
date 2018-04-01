"""Pull all profile pictures from randomuser.me and save them to images in .ico format. Also make sure copies of all images in icons/ exist in .ico format."""
from io import BytesIO
import os
from PIL import Image
import requests

num_icons = 99
url = 'https://randomuser.me/api/portraits/thumb/'
gendered_urls = ['women/', 'men/']

for gender in gendered_urls:
    for icon in range(1, num_icons + 1):
        print(gender, icon)
        if not os.path.exists('images/%s%d.ico' %(gender, int(icon))):
            response = requests.get(url + gender + str(icon) + '.jpg')
            img = Image.open(BytesIO(response.content))
            # https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python
            img.save('images/%s%d.ico' %(gender, int(icon)))

icons = os.listdir('icons/')
for img in icons:
    if img[len(img) - 3:] != 'ico':
        if not os.path.exists('icons/%sico' %img[:-4]):
            copy = Image.open('icons/' + img)
            path = 'icons/' + img[:len(img) - 3] + 'ico'
            print(path)
            copy.save(path)