import urllib2
import simplejson as json
import cloud

access_token="AAAAAAITEghMBAFjp7Nv7nHUP2dj9WorN1ugYeoLUvZAIgvzyXy5AAxyNk91pMxSUIGkZCG8d9PoTwtaOFMEa6bVInQdJgDpIh1KSjYGwZDZD"

def getLikePages(profile_id):
	all_likes=urllib2.urlopen('https://graph.facebook.com/'+profile_id+'/likes?access_token='+str(access_token))
	all_likes=json.loads(all_likes.read())
	return all_likes['data']

def getLikeCount(like_page_list):
	count = len(like_page_list)
	count_spec=0
	for i in range(0,count) :
		cat=like_page_list[i]['category']
		cat=str(cat)
		if cat == "Non-profit organization" or cat == "Community": 
			count_spec+=1
			#print cat
		else:
			pass
	count_info = {
		"community_count":count_spec,
		"total_community_count":count
	}
	return count_info

def getFriends():
	all_friends=urllib2.urlopen('https://graph.facebook.com/me/friends?fields=id,name&access_token='+str(access_token))
	all_friends=json.loads(all_friends.read())
	#print all_friends

#	friend_ids=[]
#	for i in range(0,len(all_friends['data'])-1):
#		pid=str(all_friends['data'][i]['id'])
#		name=all_friends['data'][i]['name']
#		friend_ids.append(pid+","+name)
#	all_likes=urllib2.urlopen('https://graph.facebook.com/rajibsg/likes?access_token='+str(access_token))
#	all_likes=json.loads(all_likes.read())
#	likes_current=[]
#	for i in range(0,len(all_likes['data'])):
#		likes_current.append(all_likes['data'][i])
#	likes['rajibsg']=likes_current
#	print likes
#getLikesStat()
	
	#print all_friends['data']
	return all_friends['data']

def controller():
	all_friends=getFriends()
	print all_friends

	list_friend_likes=[]

	count_friends=len(all_friends)
	for i in range(0,count_friends-1):
		friend_id=all_friends[i]['id']
		friend_likes=getLikePages(friend_id)



		friend_object={
			"id":friend_id,
			"likes":friend_likes
		}

		print friend_object
		print "****** DONE FOR "+str(i)+" user**** "

		list_friend_likes.append(friend_object)
	return list_friend_likes


	# get all friends [ {"id":"3432423" ,name:"shoubhik"} ]

	# for each friend , call getLikePages(id) . returns data[]
	# 		[ { "id" : "34343" , "pages" : data[] }]

#a=getLikePages('me')
#print getpyhtonLikeCount(a)


#controller()

op_id=cloud.call(controller)