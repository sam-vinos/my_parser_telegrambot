import requests
from bs4 import BeautifulSoup
import fake_useragent


def fakeuseragent():
    return fake_useragent.UserAgent().random

def strinint(string:str):
    string=string.replace(" ", "")
    string=string.replace(",", ".", 1)
    string=list(string)
    resint=str()
    for i in string:
        if i=='.':
            break
        elif i in "1234567890":
            resint+=i
    return int(resint)

