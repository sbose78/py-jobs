import simplejson as json
import urllib2

access_token='AAAAAAITEghMBAMEqjyPgsjWOFYdxvg3AMYgzRAew4AshlYBZCmwjrh2tvZAkNazsM9Hps7C25df36xKpjsRWcuBli548wPWawobWYy2gZDZD'
all_friends=urllib2.urlopen('https://graph.facebook.com/me/friends?access_token='+access_token)
all_friends=all_friends.read()
all_friends=json.loads(all_friends)

females=0
males=0
unspecified=0
count= len(all_friends['data'])
for i in range(0,count-1):
	if 'gender' in all_friends['data'][i].keys():
		if all_friends['data'][i]['gender'] == 'male':
			males=males+1
		else:
			females=females+1
	else:
		unspecified=unspecified+1
	print "males : "+str(males)+" females : "+ str(females)+" unspecified : "+str(unspecified)
