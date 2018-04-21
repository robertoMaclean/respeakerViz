import os

def ensureDir(file_path):
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)

def FillJson(obj):
	usersTime = obj.GetUserTime()
	usersInt = obj.GetUsersInterv()
	time = obj.GetTime()
	userStartInt = obj.GetUserStartInt()
	usersVol = obj.GetUsersVol()
	data = {
		'usersTime':[],
		'usersIntDur':[[],[],[],[]],
		'usersSpeakTimePercent':[],
		'userIntInTime': [],
		'usersVol': [[],[],[],[]],
	}
	user_num = 1
	speak_time_users = float(usersTime[0]) + float(usersTime[1]) + float(usersTime[2]) + float(usersTime[3])
	for users in usersTime:
		data['usersTime'].append({'x':'Usuario '+str(user_num),'y':users})
		data['usersSpeakTimePercent'].append({'label':'Porcentaje Usuario '+str(user_num),'value':"{0:.2f}".format((float(users)/speak_time_users)*100)})
		user_num += 1
	user_num = 0
	#print(usersInt)
	#print(usersInt)
	for users in usersInt:
		#print('users', users)
		for interv in range(0,len(users)):		
			data['usersIntDur'][user_num].append({'x':str(interv+1),'y':"{0:.2f}".format(users[interv][-1]-users[interv][0])})		
		user_num += 1
	a=b=c=d=0
	data['userIntInTime'].append({'y':0,'a':a, 'b':b, 'c':c, 'd':d})	
	for pos in range(0, len(userStartInt[0])):
		if userStartInt[0][pos] == 1:
			a += 1
		elif userStartInt[0][pos] == 2:
			b += 1
		elif userStartInt[0][pos] == 3:
			c += 1
		elif userStartInt[0][pos] == 4:
			d += 1
		data['userIntInTime'].append({'y':userStartInt[1][pos],'a':a, 'b':b, 'c':c, 'd':d})
	pos = 1
	coef = int()
	for vol, user, time in usersVol:
		if pos == 4:
			a=b=c=d=0
			if user == 1:
				a = vol
			elif user == 2:
				b = vol
			elif user == 3:
				c = vol
			else:
				d = vol
			data['usersVol'][0].append({'y':time,'a':a})
			data['usersVol'][1].append({'y':time,'b':b})
			data['usersVol'][2].append({'y':time,'c':c})
			data['usersVol'][3].append({'y':time,'d':d})
			pos = 0
		pos += 1
	return data


