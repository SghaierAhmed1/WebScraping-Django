from requests import get
from bs4 import BeautifulSoup
import urllib.request
import json
data={}
data["cdis"]={}
def get_url(url,online=True):
    if online :
        r=get(url)
        if r.status_code==200:
            return r.text
        else:
            return None
    else:
        try:
            f=open(url,"r")
        except:
            return None
        else:
            f.read()
            f.close

def get_links(url):
    t=get_url(url)
    if t!=None:
        b=BeautifulSoup(t,"lxml")
        l=b.find_all("a" , class_="jsPrdtBILA prdtBILA")
        L=[]
        for e in l:            
            L.append(e["href"])
        return L
def get_name(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("title")
    ch=c.text
    ch2=""
    if ("Câble" not in ch and "CÂBLE" not in ch and "Console" not in ch and "PACK" not in ch and "Sac" not in ch and "MANETTE " not in ch and "Outil" not in ch and "pcs" not in ch and "ligne" not in ch and "PACK"):
        if ("Jeu" in ch):
            ch2=ch.split("Jeu")[0]
        else:
            ch2=ch.split("SONY")[0]   
    return ch2

def get_allnames(l):
    for i in l:
        get_name(i)

def get_price(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("span" , class_="fpPrice price jsMainPrice jsProductPrice hideFromPro")
    return c.text
    
def get_genre(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    l=b.find("div" , class_="fpBulletPointReadMore").find_all("li")
    for i in l:
        if ("Genre du jeu vidéo" in i.text):
            ch=i.text
            ch1=ch.split(":")[1]
            ch2=ch1.split("\r")[0]
            print(ch2)
            return(ch2)
    
def get_img(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("div" , class_="fpMainImg")
    g=(c["data-zurl"])
    t1=get_url(g)
    b1=BeautifulSoup(t1,"lxml")
    c1=b1.find("div" , class_="ImgZoomPop").find("img")
    return(c1["src"])
    
def get_info(url):
    global data
    a=get_name(url)
    b=get_genre(url)
    c=get_price(url)
    j=get_img(url)
    d={}
    if (a!=None and b!=None and c!=None):
        h="work"
        data["cdis"][a]={"Genre":b,"Prix":c,"Image":j}

def get_allinfo(l):
    for i in l:
        get_info(i)
    h="cdis" 
    n=(json.dumps(data, sort_keys=True, indent=4))
    with open("C:\\Users\\Bouhmid\\Desktop\\Projet\\Try\\"+h+".txt","a") as f:
        f.write(n)
    print(n)
    


l=get_links("https://www.cdiscount.com/jeux-pc-video-console/r-magasin+en+ligne+jeux+video.html#_his_")
#print(l)
#get_allnames(l)
get_allinfo(l)
#get_img("https://www.cdiscount.com/jeux-pc-video-console/ps4/dirt-rally-2-0-deluxe-edition-jeu-ps4/f-1030401-4020628751982.html?idOffre=330193618#cm_sp=PA:9810777:NH:CAR")
#get_info("https://www.cdiscount.com/jeux-pc-video-console/ps4/call-of-duty-modern-warfare-jeu-ps4/f-1030401-5030917285202.html#read")
