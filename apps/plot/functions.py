import os

def ensureDir(file_path):
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)

def FillJson(obj):
	usersTime = obj.GetUserTime()
	usersInt = obj.GetUsersInterv()
	time = obj.GetTime()
	userStartInt = obj.GetUserStratInt()
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
		data['usersIntDur'][user_num] = []
		for interv in range(0,len(users)-1):		
			data['usersIntDur'][user_num].append({'x':str(interv+1),'y':"{0:.2f}".format(users[interv][-1]-users[interv][0])})
			
		user_num += 1
	a=b=c=d=0
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
	return data


