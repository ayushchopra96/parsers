from bs4 import BeautifulSoup
import urllib
import os,time
def fetchurl(geturl):
	'''Supply the url to download the required file'''
	r=urllib.urlopen(geturl).read()
	soup=BeautifulSoup(r)
	links=soup.find_all("a",class_="pl-video-title-link")
	target=open("urls.txt","w")
	for link in links:
		link=link.get('href')
		link="http://www.youtube.com"+link
		target.write(link)
		target.write("\n")
		download(link)
	
	target.close()
	print len(links)

def download(url):
	'''takes url and downloads a video'''
	print "downloading..."
	termcommand="youtube-dl "+ url
	os.system(termcommand)
	time.delay(25)

fetchurl("http://www.youtube.com/playlist?list=PL442FA2C127377F07")
'''
fp=open("urls.txt")
	c=fp.read()
	while c is not None:
		download(c)
'''