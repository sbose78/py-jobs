access_token="AAAAAAITEghMBAGf8kXPSeulH7DxTW2ZCTpulYQ1CFvftufmSah5QL3N0ZCsY4Wm9MQMvieL53ZCKnZBvpUl2A7Dgy4On8ynOMX1FSw5IwwZDZD"
import urllib2
import simplejson as json


all_likes=urllib2.urlopen('https://graph.facebook.com/rajibsg/likes?access_token='+str(access_token))

all_likes=json.loads(all_likes.read())

count = len(all_likes['data'])

count_spec=0

for i in range(0,count):
	cat=all_likes['data'][i]['category']
	cat=str(cat)
	if cat == "Non-profit organization" or cat == "Community": 
		count_spec+=1
		print cat
	else:
		pass

percentage=(count_spec/(double)count)*100
print count
print count_spec
print percentage