#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
import pandas as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup
import re
import string
from string import digits

dictionary={}

matrix_paper=pd.read_csv("paper.csv")
matrix_author=pd.read_csv("author.csv")
matrix_org=pd.read_csv("org.csv")
matrix_term=pd.read_csv("term.csv")

dictionary['paper']='class_paper'
dictionary['author']='class_author'
dictionary['organization']='class_organization'
dictionary['term']='class_term'
dictionary['data mining']='paper'
dictionary['john']='author'

# print type(matrix_term)

paper_arr=matrix_paper.as_matrix()
author_arr=matrix_author.as_matrix()
org_arr=matrix_org.as_matrix()
term_arr=matrix_term.as_matrix()

for i in range(paper_arr.shape[0]-1):
	temp = str(paper_arr[i][0])
	dictionary[temp[:-1]]="paper"

for i in range(author_arr.shape[0]):
	temp = str(author_arr[i][0])
	dictionary[temp]="author"


for i in range(org_arr.shape[0]):
	temp = str(org_arr[i][0])
	dictionary[temp]="organization"

for i in range(term_arr.shape[0]):
	temp = str(term_arr[i][0])
	dictionary[temp]="term"


#print dictionary
print dictionary['data mining']
query=raw_input("Enter your query\n")

query= query.lower()

#print query

stopwords = ['a','an','is','a','at','is','by','the','that','were','from','in','on']
querywords = query.split()

resultwords  = [word for word in querywords if word.lower() not in stopwords]
query_input = ' '.join(resultwords)

print 'after removing stopwords query is ',query_input

items=query_input.split()
bigrams=[]
for i in range(len(items)-1):
	bigrams.append((items[i],items[i+1]))

#print 'bigrams are ',bigrams
#print len(bigrams)

ner={}
for i in range(len(bigrams)):
	b=bigrams[i][0]+' '+bigrams[i][1]
	if dictionary.get(b)!=None:
		ner[b]=dictionary.get(b)
		query_input=query_input.replace(b,'')

#print ner
#print query_input
#print bigr

#print items
for i in items:
	if dictionary.get(i)!=None:
		ner[i]=dictionary.get(i)
		query_input=query_input.replace(i,'')

print ner
#print ner['data mining']

'''

#--------------------------------------------PARSING-------------------------------------------------------------

from nltk.parse.stanford import StanfordDependencyParser

final_dependency = []
sentence = query
dependency_tree = StanfordDependencyParser()
dependency_parser = dependency_tree.raw_parse(sentence)

parsetree = list(dependency_parser)[0]
# print parsetree.nodes.values()
# print  ""

# print type(dependency_parser)

for k in parsetree.nodes.values():
	# print k
	if k["head"] == 0:
		final_dependency.append(str(k["rel"]) + ',' + "Root" + "," + str(k["word"]))
# print final_dependency


# from nltk.parse.stanford import StanfordDependencyParser
# stan_dep_parser = StanfordDependencyParser() 

dependency_parser = dependency_tree.raw_parse(sentence)

# print type(dependency_parser)

# try:
# dependency_parser = dependency_parser
dep = dependency_parser.next()
for triple in dep.triples():
	# print triple[1],"(",triple[0][0],", ",triple[2][0],")"
	final_dependency.append(str(triple[1]) + "," + str(triple[0][0]) + "," +  str(triple[2][0]))
# except StopIteration:
	# dependency_

# print "HELLO"
for i in final_dependency:
	print i


final_dependency1 =[]

for i in range(len(final_dependency)):
	splitFinal = final_dependency[i].split(',')
	y=''
	for j in splitFinal:
		if j == "Retrieval" or j == "retrieval":
			x = "information retrieval"
			y = y + x + ','
		elif j == 'Mining' or j == 'mining':
			x = 'data mining'
			y = y + x + ','
		else:
			if j != "compound":
				y = y + j + ','
			else:
				i=i+1
				break
	final_dependency1.append(y)


print "------------------------------------------------------"

final_dependency1=list(filter(None,final_dependency1))

for i in final_dependency1:
	print i

# ------------------------------3.5 GRAPH DEPENDENCIES-------------------------

GR=[]
CR=[]
subjet=[]
object=[]
for i in range(len(final_dependency)):
	splitFinal = final_dependency[i].split(',')
	if dictionary.get(splitFinal[1])!=None and dictionary.get(splitFinal[2])!=None:
		if splitFinal[0] != 'conj':
			res = []
			res.append(splitFinal[1] + ',' + splitFinal[2])
			GR.append(res)

	if dictionary.get(splitFinal[1])!=None or dictionary.get(splitFinal[2])!=None:
		if splitFinal[0] == 'acl:relcl':
			CR.append(splitFinal[0])
			subject.append(splitFinal[1])
		if splitFinal[0] == 'nmod' or splitFinal[0] == 'dobj':
			CR.append(splitFinal[0])
			object.append(splitFinal[2])

for i in range(len(subject)):
	p=str(subject[i]+','+object[i])
	GR.append(p)	


print CR
print ""
print GR

'''

#--------------------------------------------PARSING-------------------------------------------------------------

url = "http://nlp.stanford.edu:8080/parser/index.jsp"
data = {
	"query": query,
	"parse": "Parse"
}

with requests.Session() as session:
	session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
	session.get(url)
	response = session.post(url, data=data)
	soup = BeautifulSoup(response.content, 'html.parser')
	result = soup.findAll("div", {"class":"parserOutput"})
	parse_output=result[2].text.splitlines()
#print parse_output

final_dependency=[]

for i in range(len(parse_output)):
	if(parse_output[i]!=''):
		final_dependency.append(str(parse_output[i]))

print final_dependency

#print type(final_dependency[0])


c=0
new_str=""
for i in range(len(final_dependency)):
	c=0
	if "information" in final_dependency[i]:
		new_str=string.replace(final_dependency[i],"information","information retrieval")
		c=1
	if "retrieval" in final_dependency[i] and c==0:
		new_str=string.replace(final_dependency[i],"retrieval","information retrieval")
		c=1
	if(c==1):
		del final_dependency[i]
		final_dependency.insert(i,new_str)


for i in range(len(final_dependency)):
	c=0
	if "data" in final_dependency[i]:
		new_str=string.replace(final_dependency[i],"data","data mining")
		c=1
	if "mining" in final_dependency[i] and c==0:
		new_str=string.replace(final_dependency[i],"mining","data mining")
		c=1
	if(c==1):
		del final_dependency[i]
		final_dependency.insert(i,new_str)
		
#print final_dependency

for i in range(len(final_dependency)):
	new_str=string.replace(final_dependency[i],"-","")
	del final_dependency[i]
	final_dependency.insert(i,new_str)
	res = final_dependency[i].translate(None, digits)	
	del final_dependency[i]
	final_dependency.insert(i,res)
	new_str=string.replace(final_dependency[i],"(",",")
	del final_dependency[i]
	final_dependency.insert(i,new_str)
	new_str=string.replace(final_dependency[i],")","")
	del final_dependency[i]
	final_dependency.insert(i,new_str)
	new_str=string.replace(final_dependency[i],", ",",")
	del final_dependency[i]
	final_dependency.insert(i,new_str)
	

print final_dependency

'''for i in range(len(final_dependency)):
	p1=final_dependency[i].split('(')
	#print p1[1]
	p2=p1[1].split(',')
	#print p2[0], p2[1]
	for j in range(2):
		p3=p2[j].split('-')
		#print p3[0],p3[1]
		p4=p3[0].strip(' ')
		if p4=="retrieval" or p4=="information":
			x="in'''

GR=[]
CR=[]
subject=[]
object_=[]
for i in range(len(final_dependency)):
	splitFinal = final_dependency[i].split(',')
	if dictionary.get(splitFinal[1])!=None and dictionary.get(splitFinal[2])!=None:
		if splitFinal[0] != 'conj'and splitFinal[0] != 'compound':
			penta = []
			penta.append(splitFinal[1] + ',' + splitFinal[2])
			GR.append(penta)

	elif dictionary.get(splitFinal[1])!=None or dictionary.get(splitFinal[2])!=None:
		if splitFinal[0] == 'acl:relcl' or splitFinal[0] == 'dep':
			CR.append(splitFinal[0])
			subject.append(splitFinal[1])
		if splitFinal[0] == 'nmod' or splitFinal[0] == 'dobj':
			CR.append(splitFinal[0])
			object_.append(splitFinal[2])
print subject
print object_

for i in range(len(subject)):
	if(object_[i]!=''):
		potti=str(subject[i]+','+object_[i])
		GR.append(potti)	


print CR
print ""
print GR








