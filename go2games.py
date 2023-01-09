from requests import get
from bs4 import BeautifulSoup
import json
data={}
data["G2G"]={}
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
        l=b.find_all("a" , class_="product-item-link more")
        L=[]
        for e in l:            
            L.append(e["href"])
        return L

def get_name(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("div" , class_="page-title-wrapper product").find("h1" , class_="page-title").find("span" , class_="base")
    ch=c.text
    if ("/" not in ch and "<" not in ch and ">" not in ch and "|" not in ch) :
        return ch
            
def get_allnames(l):
    for i in l:
        get_name(i)
        
def get_genre(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    l=[]
    for i in b.findAll("tr"):
        for c in i.findAll("td"):
            for j in i.findAll("th"):
                if (j.text=="Genre"):                    
                    return(c.text)
def get_img(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("img" , class_="fotorama__img")
    if c:
        print("yes")
    else:
        print("no")
        
def get_price(url):
    t=get_url(url)
    b=BeautifulSoup(t,"lxml")
    c=b.find("span" , class_="price-container price-final_price tax weee").find("span" , class_="price")
    return(c.text)
def get_info(url):
    global data
    a=get_name(url)
    b=get_genre(url)
    c=get_price(url)
    d={}
    if (a!=None and b!=None and c!=None):
        h="work"
        data["G2G"][a]={"Genre":b,"Prix":c}

def get_allinfo(l):
    for i in l:
        get_info(i)
    h="work" 
    n=(json.dumps(data, sort_keys=True, indent=4))
    with open("C:\\Users\\Bouhmid\\Desktop\\Projet\\Try\\"+h+".txt","a") as f:
        f.write(n)
    print(n)
    

                    
        
        
        
#l=get_links("https://www.go2games.com/pc")
#h="work"
#with open("C:\\Users\\Bouhmid\\Desktop\\Projet\\Try\\"+h+".txt","a") as f:
 #   f.close()
get_img("https://www.go2games.com/playstation-4/assassins-creed-valhalla-gold-edition-ps4")
#print(l)
#b=get_allnames(l)
#print(b)
#get_allinfo(l)

            
