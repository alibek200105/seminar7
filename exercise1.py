try:
	file1=open('brown.txt')
except:
	print('File cannot be opened:', file1)
	exit()
lines=file1.readlines()
file1.close()
diction={}
file2=open('output.txt','w')

for line in lines:
	words=line.split()
	length=len(words)

	for i in range(length-7):
		key=words[i]+' '+words[i+1]+' '+words[i+2]+' '+words[i+3]+' '+words[i+4]+' '+words[i+5]+' '+words[i+6]
		if key not in diction:
			diction[key]=1
		else:
			diction[key]+=1

max=None
for key in diction:
	result=key,diction[key]
	file2.write(str(result))
	file2.write('\n')
	if max is None or diction[key]>max:
			max=diction[key]
print('Max:',max)

