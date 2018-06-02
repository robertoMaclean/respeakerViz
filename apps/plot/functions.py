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
	usersActivity = obj.GetActivity()
	usersActivityContinuos = obj.GetActivityContinuos()
	usersRelation = obj.GetUsersRelations()
	userVolFrame = obj.GetUsersVolFrame()
	#print(usersActivity[0])
	#print(usersActivityContinuos[0])
	data = {
		'usersTime':[],
		'usersIntDur':[[],[],[],[]],
		'usersSpeakTimePercent':[],
		'userIntInTime': [],
		'usersVol': [[],[],[],[]],
		'usersVolAVG': [],
		'usersRelation': {
			"nodes": [],
			"links": []
		},
		'd3': {
			"name":"Intervenciones",
			"children": []
		},
		'usersVolFrame': [[],[],[],[]],
		'userVolFrameWhitoutSilence': [[],[],[],[]],
		'usersActivity': [[],[],[],[]],
		'usersActivityContinuos': [[],[],[],[]],
		'usersInteraction': [],
	}
	user_num = 1
	speak_time_users = float(usersTime[0]) + float(usersTime[1]) + float(usersTime[2]) + float(usersTime[3])
	for users in usersTime:
		data['usersTime'].append({'x':'Usuario '+str(user_num),'y':users})
		data['usersSpeakTimePercent'].append({'label':'Porcentaje Usuario '+str(user_num),'value':"{0:.2f}".format((float(users)/speak_time_users)*100)})
		user_num += 1
	user_num = 0

	for users in usersInt:
		#print('users', users)
		data['d3']['children'].append({"name": "Usuario"+str(user_num+1), "children": []})
		for interv in range(0,len(users)):
			time = "{0:.2f}".format(users[interv][-1]-users[interv][0])	
			start = "{0:.2f}".format(users[interv][0])	
			data['usersIntDur'][user_num].append({'x':start,'y':time})
			data['d3']['children'][user_num]['children'].append({"name": str(users[interv][0])+"-"+str(users[interv][-1]), "size":time})
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
		for vol, time in user:
			data['usersVol'][user_num].append({'x':str(time),'y':'{0:.2f}'.format(vol)})
		user_num+= 1
	user_num = 1
	for vol in usersVol:
		data['usersVolAVG'].append({'x':'Usuario '+str(user_num),'y':'{0:.2f}'.format(vol)})
		user_num+= 1
	emisor = 1
	receptor = 1
	for x in range(len(usersRelation)):	
		if(emisor==receptor):
			receptor += 1
		data['usersInteraction'].append({'emisor':emisor,'receptor':receptor, 'value': usersRelation[x]})
		receptor += 1
		if((x+1) % 3 == 0):
			emisor += 1	
		if(receptor == 5):
			receptor = 1
	user_num = 0
	prom_len_userVolFrame = (len(userVolFrame[0])+len(userVolFrame[1])+len(userVolFrame[2])+len(userVolFrame[3]))
	max_data_plot = int((prom_len_userVolFrame)/500)
	index = 0
	volsum = 0
	volsumNoSilence = 0
	firstime = True
	# print(prom_len_userVolFrame/max_data_plot)
	# print(max_data_plot)
	i = 0
	for user in userVolFrame:
		index = 0
		indexNoSilence = 1
		for vol, time in user:
			if(firstime and float(vol)>0):
				firstime = False

			if(float(vol)>0):
				indexNoSilence += 1
				volsumNoSilence = volsumNoSilence + float(vol) 
			if not firstime:
				index+=1
				volsum = volsum + float(vol)
				if (max_data_plot==index):
					data['usersVolFrame'][user_num].append({'x':time,'y':'{0:.2f}'.format(volsum/max_data_plot)})
					data['userVolFrameWhitoutSilence'][user_num].append({'x':time,'y':'{0:.2f}'.format(volsumNoSilence/indexNoSilence)})
					volsum = 0
					index = 0
					volsumNoSilence = 0 
					indexNoSilence = 1
		user_num+= 1
	for i in range(len(usersActivity)):
		index = 0
		time = 0
		for val in usersActivity[i]:
			if time == 0:
				time = val
			if index%20 == 0:
				while(time < val):
					data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
					data['usersActivityContinuos'][i].append({'x':float('{0:.2f}'.format(time)),'y':1})
					time += 20*0.02
				data['usersActivity'][i].append({'x':val,'y':1})
				data['usersActivityContinuos'][i].append({'x':val,'y':1})
			time = val+20*0.02
			index += 1
	# for i in range(len(usersActivityContinuos)):
	# 	index = 0
	# 	time = 0
	# 	for val in usersActivityContinuos[i]:
	# 		if time == 0:
	# 			time = val
	# 		if index%20 == 0:
	# 			data['usersActivityContinuos'][i].append({'x':val,'y':1})
	# 		index += 1
	return data
	

