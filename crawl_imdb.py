import requests,bs4
movie_links=[] #use a set to avoid repetition of visited links
movie_info=[]
def parsePage(soup):
	global movie_info
	try:
		schema_div=soup.find('div',{'id':'pagecontent'})
		if(not (schema_div.has_attr('itemtype') and schema_div['itemtype']=='http://schema.org/Movie')):
			return;
		movie={};
	try:
		content_div = soup.find('div',{'id':'title-overview-widget'})
		movie['title']=content_div.select('h1.header > span.itemprop')[0].text		#select() method of bs4 returns a list,even if one element
		movie['year']=content_div.select('h1.header > span.nobr > a')[0].text
		movie['rating']=content_div.select('div.star-box-giga-star')[0].text
		movie['director']=[]
		movie['url']=url
		for i in content_div.select('div[itemprop=director] > a span'):
			movie['director'].append(i.text)
		movie_info.append(movie)
		print(movie)
	except(Exception):
		return

def process_request(url):
	res=requests.get(url)
	print('request received')
	soup=bs4.BeautifulSoup(res.text)
	parsePage(soup)
	a_list=soup.find_all('a')
	print(len(a_list))
	rel-movie_links=set()
	for anchor in a_list:
		if (anchor.has_attr('href')):
			url=anchor['href']
			if (url.find('/title/tt')==0):               #.find() method of a string returns begin index of the sunstring
				url=url.split('?')[0]
				"/".join(url.split('/')[:3])			#to join items of a list together.			
				rel-movie_links.add('http://imdb.com'+url);
	return rel-movie_links

count=0
movie_links=list(process_request('http://www.imdb.com'))
i=0
while i<len(movie_links):
	temp= process_request(movie_links[i])
	for (j not in movie_links):
		movie_links.append(j)
	i=i+1