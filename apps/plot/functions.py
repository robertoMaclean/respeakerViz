import os

def ensureDir(file_path):
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)

def FillJson(obj):
	usersTime = obj.GetUserTime()
	usersInt = obj.GetUsersInterv()
	time = obj.GetTime()
	data = {
		'usersTime':[],
		'usersIntDur':[[],[],[],[]],
		'usersInterv':[],
		'usersSpeakTimePercent':[],
		'userIntInTime': []
	}
	user_num = 1
	speak_time_users = float(usersTime[0]) + float(usersTime[1]) + float(usersTime[2]) + float(usersTime[3])
	for users in usersTime:
		print(users)
		data['usersTime'].append({'x':'Usuario '+str(user_num),'y':users})
		data['usersSpeakTimePercent'].append({'label':'Porcentaje Usuario '+str(user_num),'value':"{0:.2f}".format((float(users)/speak_time_users)*100)})
		user_num += 1
	user_num = 0
	#print(usersInt)

	for users in usersInt:
		usuario = 'user'+str(user_num)
		data['usersIntDur'][user_num] = []
		a = b = c = d = 0
		for interv in range(0,len(users)-1):
			res = users[interv][0]
			if user_num == 0:
				a += 1
			elif user_num == 1:
				b += 1
			elif user_num == 2:
				c += 1
			elif user_num == 3:
				d += 1
			
			data['usersIntDur'][user_num].append({'x':str(interv+1),'y':"{0:.2f}".format(users[interv][-1]-users[interv][0])})
			data['userIntInTime'].append({'y':res,'a':a, 'b':b, 'c':c, 'd':d})
		user_num += 1
	return data


