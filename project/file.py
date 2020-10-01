import re
import pandas as pd

textfile=open("new.txt","r")

author=[]

for l in textfile:
	print l
	if re.match("^#@.*",l):
		author.append(l[3:])


textfile.seek(0)

org=[]

for line in textfile:
	if re.match('^#o.*',line):
		org.append(line[3:])


textfile.seek(0)

term=[]

for line in textfile:
	if re.match('^#t.*',line):
		term.append(line[3:])

textfile.seek(0)

source=[]

for line in textfile:
	if re.match('^#c.*',line):
		source.append(line[3:])

final=[]



for i in range(len(source)):
	p=[]
	p.append(author[i])
	p.append(org[i])
	p.append(term[i])
	p.append(source[i])
	final.append(p)
	

df=pd.DataFrame(final)
df.to_csv("Data.csv",header=False,index=False)

