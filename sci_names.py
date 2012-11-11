f_source=open('/root/udhc-openshift/botanical-names.txt','r')
f_destination=open('/root/udhc-openshift/botanical-names-new3.txt','w')

for line in f_source:
	if '#' in line:
		splitted=line.split('#')
		word=splitted[1]
		word2=word.lstrip()	
		f_destination.write(word2)
	elif '*' in line:
		splitted=line.split('*')
		word=splitted[1]
		word2=word.lstrip()
		f_destination.write(word2)
	else:
		pass

