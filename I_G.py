from requests import get
from bs4 import BeautifulSoup
import urllib.request
import json
data={}
data["IG"]={}
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
        l=b.find_all("a" , class_="cover")
        L=[]
        for e in l:            
            L.append(e["href"])
        return L
def get_img(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    l=[]
    c=b.find("div" , class_="product").find("img")
    if c:
        return(c["src"])
def all_img(l):
    for i in l:
        get_img(i)
       
def get_name(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("div" , class_="title").find("h1")
    return(c.text)
    
def get_genre(url):
    s=0
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    l=b.find("div" , class_="tags").find("a" , class_="tag tag1")
    d=b.find("div" , class_="tags").find("a" , class_="tag tag8")
    c=b.find("div" , class_="tags").find("a" , class_="tag tag32")
    j=b.find("div" , class_="tags").find("a" , class_="tag tag15")
    if l:
        return(l["content"])
    elif d:
        return(d["content"])
    elif c:
        return(c["content"])
    elif j:
        return(j["content"])
    else:
        s=1
        
def get_price(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("div" , class_="prices").find("div" , class_="price")
    return(c.text)
def get_info(url):
    global data
    a=get_name(url)
    b=get_genre(url)
    c=get_price(url)
    j=get_img(url)
    d={}
    if (a!=None and b!=None and c!=None):
        h="work"
        data["IG"][a]={"Genre":b,"Prix":c,"Image":j}

def get_allinfo(l):
    for i in l:
        get_info(i)
    h="instant" 
    n=(json.dumps(data, sort_keys=True, indent=4))
    with open("C:\\Users\\Bouhmid\\Desktop\\Projet\\Try\\"+h+".txt","a") as f:
        f.write(n)
    print(n)
def down_img(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    l=[]
    c=b.find("div" , class_="product").find("img")
    temp=c["src"]
    if temp[:1]=="/":
        image="https://www.instant-gaming.com/en/" + temp
    else:
        image=temp
    filename=c["alt"]
    imagefile=open(filename + ".jpeg" , "wb")
    ##### J'ai juste utilisé get(img).content pour avoir le contenu de l'image
    imagefile.write(get(image).content)
    imagefile.close()
h="instant"    
with open("C:\\Users\\Bouhmid\\Desktop\\Projet\\Try\\"+h+".txt","a") as f:
    f.close()
l=get_links("https://www.instant-gaming.com/en/")
#print(l)
#s=all_img(l)
#print(s)
#get_allinfo(l)
get_allinfo(l)
#down_allimg(l)
#down_info("https://www.instant-gaming.com/en/840-buy-key-gogcom-cyberpunk-2077/")

