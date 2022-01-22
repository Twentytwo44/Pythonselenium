from email.errors import MessageError
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from songline import Sendline
import time
token = "JgmVILuhN8LSEGhXhopTsvlX9786EpbUpUsTdoSagJT"
messenger = Sendline(token)



driverpath = r'C:\Users\User\Desktop\sele\driverch\chromedriver.exe'

opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome(driverpath,options=opt)

def Twitterpost(twitter_name):
    url = 'https://twitter.com/{}'.format(twitter_name)
    driver.get(url)
    time.sleep(30)

    page_html = driver.page_source #print out html 


    data = soup(page_html, 'html.parser')

    posts = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
    founddot = False
    allp = []
    for p in posts:
        txt = p.text
        if founddot == True:
            allp.append(txt)
            founddot = False
        if txt == '·':
            founddot = True
   
    return allp

checktwitter = ['elonmusk','BillGates']
for ct in checktwitter:
    post = Twitterpost(ct)
    print('-----------{}-------'.format(ct))
    messenger.sendtext('---------{}-------'.format(ct))
    for p in post:
        print(p)
        messenger.sendtext(p)


driver.close()