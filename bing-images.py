from bs4 import BeautifulSoup
import requests

'''To parse images for a particular keyword from bing images '''
'''To run this script,import the module bing-images.py and then run the function  scrape with the keyword as argument '''
#target=open("urls.txt","w")
def scrape(key):
  url="https://www.bing.com/images/search/?q="+key+"&form=QBIR&pq="+key+"&sc=8-12&sp=-1&sk="
  r=requests.get(url)
  soup=BeautifulSoup(r.content)
  links=soup.find_all("img")
  print len(links)
  for link in links:
      print link
      #target.write("\n")
      #new_url="https://www.bing.com"+x

#scrape("inscriptions")
