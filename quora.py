from requests import session
from bs4 import BeautifulSoup
from PIL import Image
import sys
import os
import urllib

def main():
    if len(sys.argv) < 3:
        print "Usage: python quora.py [FirstName] [MiddleName] [LastName] \nThe first letter of each word of the name must be uppercase"
        sys.exit()
    else:
        pass
    name = sys.argv
    login(name)


def login(profile):

    name = profile[1] + ' ' + profile[2]
    nameurl = profile[1] + '-' + profile[2]
    url = "https://www.quora.com/profile/" + nameurl
    status_OK = 200
    payload = {
    'email' : 'sankhla.dileep96@gmail.com',
    'password' : 'Hakimpet@96'
    }

    with session() as c:
        c.post("https://www.quora.com/?", data = payload)
        r = c.get(url)
        if r.status_code != status_OK:
            print "Sorry! Profile not found as", nameurl
            print "URL :", url, "not found"
            sys.exit()

        print "...profile found!"

        page = r.text.encode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        followers = int(soup.select_one("a[href*=followers] .list_count").get_text())
        print "...followers :", followers

        print "...downloading profile picture..."

        directory = "profile pic"
        if not os.path.exists(directory):
            os.makedirs(directory)

        name = "./profile pic/" + name + ".jpg"
        img = soup.find('img',{'class':'profile_photo_img'})
        urllib.urlretrieve(img['src'], name)
        img = Image.open(name)
        img.show()


if __name__ == "__main__":
    main()
