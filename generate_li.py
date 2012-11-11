f_source=open('/root/python_codes/pics.txt','r')
f_destination = open('/root/python_codes/pics_output.txt','w')
for line in f_source:
	line=line.split(',')[0]
	li = "<li> <a href= \""+line+"\"><img height='200px' width='200px' src=\""+ line+  " \"/>   </a> </li>"
	f_destination.write(li)
	print li
	print "\n"


	