from pymongo.connection import Connection
f_source=open('/root/udhc-openshift/botanical-names-new3.txt','r')
connection=Connection('mongodb://sbose78:ECDW=19YRS@staff.mongohq.com:10068/BOSE')
db=connection['BOSE']
collection=db['scientific_name']
for line in f_source:
	data={
			"name":line ,
			"status":"unused"
	}
	collection.insert(data)
	print data

	
