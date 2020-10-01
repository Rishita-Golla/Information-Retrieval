import requests
from bs4 import BeautifulSoup
import re

url = "http://nlp.stanford.edu:8080/parser/index.jsp"
data = {
	"query": "papers on information retrieval and data mining",
	"parse": "Parse"
}

with requests.Session() as session:
	session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
	session.get(url)
	response = session.post(url, data=data)
	soup = BeautifulSoup(response.content, 'html.parser')
	result = soup.findAll("div", {"class":"parserOutput"})
	print result[2].text
	































