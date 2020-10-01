import numpy as np
import pandas as pd

df=pd.read_csv('Data.csv')

data=df.as_matrix()
row,col=data.shape
# print row
# # print col

# final_author=[]
# for i in range(row):    
# 	temp=data[i][1]
# 	s = temp.split(";")
# 	for j in range(len(s)):
		# if(s[j].endswith('\n')):
		# 	temp1=s[j].strip('\n')
		# 	if(temp1!=""):
		# 		final_author.append(temp1)
		# else:
		# 	final_author.append(s[j])

# final_org=[]
# for i in range(row):    
# 	temp=data[i][2]
# 	s = temp.split(";")
# 	for k in range(len(s)):
# 		t = s[k].split(',')[0]
# 		if(t.endswith('\n')):
# 			temp1=t.strip('\n')
# 			if(temp1!="" and temp1!="-"):
# 				final_org.append(temp1)
# 		elif(t!="-"):
# 			final_org.append(t)

final_term=[]
for i in range(row):    
	temp=data[i][3]
	final_term.append(temp)

# textfile=open('paper_data.txt','r')
# final_paper=[]
# for i in textfile:
# 	final_paper.append(i)

# textfile.seek(0)

final_term.sort()

author=pd.DataFrame(final_term)
author.to_csv("term.csv",header=False,index=False)