import os

def ensureDir(file_path):
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)

def FillJson(obj):
	usersTime = obj.GetUserTime()
	usersInt = obj.GetUsersInterv()
	data = {
		'usersTime':[],
		'usersIntDur':[[],[],[],[]],
		'usersInterv':[],
	}
	user_num = 1
	for users in usersTime:
		data['usersTime'].append({'x':'Usuario '+str(user_num),'y':users})
		user_num += 1
	user_num = 0
	#print(usersInt)
	for users in usersInt:
		usuario = 'user'+str(user_num)
		data['usersIntDur'][user_num] = []
		for interv in range(0,len(users)-1):
			#print(users[interv])
			data['usersIntDur'][user_num].append({'x':str(interv+1),'y':"{0:.2f}".format(users[interv][-1]-users[interv][0])})
		user_num += 1
	return data


