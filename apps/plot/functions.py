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
	usersVolInterv = obj.GetUsersVolPromInterv()
	data = {
		'usersTime':[],
		'usersIntDur':[[],[],[],[]],
		'usersSpeakTimePercent':[],
		'userIntInTime': [],
		'usersVol': [[],[],[],[]],
		'usersRelation': {
			"nodes": [],
			"links": []
		},
		'd3': {
			"name":"Intervenciones",
			"children": []
		},
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
		data['d3']['children'].append({"name": "Usuario"+str(user_num+1), "children": []})
		for interv in range(0,len(users)):
			time = "{0:.2f}".format(users[interv][-1]-users[interv][0])	
			start = "{0:.2f}".format(users[interv][0])	
			data['usersIntDur'][user_num].append({'x':str(interv+1),'y':time})
			data['d3']['children'][user_num]['children'].append({"name": "Inicio "+str(time), "size":time })
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
		
		data['usersRelation']['nodes'].append({'gender': pos+1, "group": "Usuario "+str(userStartInt[0][pos])})
		if(pos < len(userStartInt[0])-1):
			data['usersRelation']['links'].append({'source': pos, "target": pos+1})
		data['userIntInTime'].append({'y':userStartInt[1][pos],'a':a, 'b':b, 'c':c, 'd':d})
	pos = 1
	user_num = 0
	for user in usersVolInterv:
		interv = 1
		for vol in user:
			data['usersVol'][user_num].append({'x':str(interv),'y':'{0:.2f}'.format(vol)})
			interv += 1
		user_num+= 1
	return data

