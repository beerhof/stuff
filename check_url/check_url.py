import requests
import winsound, sys
import random
from time import sleep


while True:
    try:
        request = requests.get("http://www.onet.pl")
    except requests.exceptions.RequestException as e:
        continue
    if request.status_code == 200:
        winsound.PlaySound("police.wav", winsound.SND_FILENAME)
        print("strona dziala")
        break
    else:
        sleep(random.randint(10,30))

