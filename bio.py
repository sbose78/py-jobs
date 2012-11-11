import simplejson as json
import urllib2

access_token='AAAAAAITEghMBAMEqjyPgsjWOFYdxvg3AMYgzRAew4AshlYBZCmwjrh2tvZAkNazsM9Hps7C25df36xKpjsRWcuBli548wPWawobWYy2gZDZD'
all_friends=urllib2.urlopen('https://graph.facebook.com/me/friends?fields=id,name,bio&access_token='+access_token)
all_friends=all_friends.read()
all_friends=json.loads(all_friends)


count= len(all_friends['data'])
for i in range(0,count-1):
	if 'bio' in all_friends['data'][i].keys():
		#print all_friends['data'][i]
		
	else:
		pass

