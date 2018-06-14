import os
import numpy as np

def ensureDir(file_path):
	directory = os.path.dirname(file_path)
	if not os.path.exists(directory):
		os.makedirs(directory)

def FillJson(obj, group):
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
	activity_time = obj.GetTime()
	# print(usersActivity[0])
	# print(usersActivityContinuos[0])
	data = {
		'time': 0,
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
			"name": group,
			"children": []
		},
		'usersVolFrame': [[],[],[],[]],
		'userVolFrameWhitoutSilence': [[],[],[],[]],
		# 'usersActivity': [[],[],[],[]],
		# 'usersActivityContinuos': [[],[],[],[]],
		'usersInteraction': [],
	}
	data['time'] = activity_time
	user_num = 1
	speak_time_users = float(usersTime[0]) + float(usersTime[1]) + float(usersTime[2]) + float(usersTime[3])
	for users in usersTime:
		data['usersTime'].append({'x':'Usuario '+str(user_num),'y':users})
		data['usersSpeakTimePercent'].append({'label':'Usuario '+str(user_num),'value':"{0:.2f}".format((float(users)/speak_time_users)*100)})
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
	# factor = (len(usersActivity[0])+len(usersActivity[0])+len(usersActivity[0])+len(usersActivity[0]))/20000
	# factor = 1
	#print(factor)
	# for i in range(len(usersActivity)):
	# 	time = 0
	# 	#for val in usersActivity[i]:
	# 	for ii in range(len(usersActivity[i])):
	# 		#print(time, val)
	# 		#print(factor)
	# 		if usersActivity[i][ii] > time:
	# 			if(usersActivity[i][ii]-usersActivity[i][ii-1]<=0.02):
	# 				data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':1})
	# 			else:
	# 				data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
	# 			time += factor
			# print(usersActivity[i][ii]-usersActivity[i][ii-1])
			# if usersActivity[i][ii] < time:
			# 	data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
			# else:
			# 	data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':1})
			
				# if (usersActivity[i][ii] - time) < factor:
				# 	data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':1})
				# else:
				# 	data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
				# time += factor
			# 	if count > 10:
			# 		data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':1})
			# 	else:
			# 		data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
			# 	time += factor
			# 	count = 0
			# else:
			# 	count += 1

			# 	while(usersActivityContinuos[i][ii] < time and ii < len(usersActivityContinuos[i])-1):
			# 		ii += 1
			# 	time += factor
			# else: 
			# 	while time < usersActivityContinuos[i][ii]:
			# 		data['usersActivity'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
			# 		time += factor
			
			
	# for i in range(len(usersActivityContinuos)):
	# 	time = 0
	# 	for ii in range(len(usersActivityContinuos[i])):
	# 		if usersActivityContinuos[i][ii] < time:
	# 			data['usersActivityContinuos'][i].append({'x':usersActivityContinuos[i][ii],'y':1})
	# 			while usersActivityContinuos[i][ii] < time and ii < len(usersActivityContinuos[i])-1:
	# 				ii += 1
	# 			time += factor
	# 		else:
	# 			while time < usersActivityContinuos[i][ii]:
	# 				data['usersActivityContinuos'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
	# 				time += factor

			# while time > usersActivityContinuos[i][ii] and ii < len(usersActivityContinuos[i])-1 :
			# 	contar += 1
			# 	ii += 1
			# if contar > 0 :
			# 	data['usersActivityContinuos'][i].append({'x':usersActivityContinuos[i][ii],'y':1})
			# else:
			# 	data['usersActivityContinuos'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
			# time += factor
			# if (val-last)>factor:
			# 	print(time, val) 
			# 	if time<val:
			# 		while(time < val):
			# 			print(time)
			# 			data['usersActivityContinuos'][i].append({'x':float('{0:.2f}'.format(time)),'y':0})
			# 			time += factor
			# 	last = val
			# 	data['usersActivityContinuos'][i].append({'x':val,'y':1})
			# 	#time += factor
	return data
	
def FillJsonGroups(groups):
	data = {
		'd3': {
			'name': 'grupos',
			'children': []
		},
		'treemap_intdur': {
			'name': 'grupos',
			'children': []
		},
		'treemap_interv': {
			'name': 'grupos',
			'children': []
		},
		'treemap_volume': {
			'name': 'grupos',
			'children': []
		},
		'groupsSpeakTime': [],
		'groupsIntervTime': [],
		'groupsInterv': [],
		'groupsVolume': [],
		'usersVolFrame': [[],[],[],[]],
		'userVolFrameWhitoutSilence': [[],[],[],[]],
		'usersActivity': [[],[],[],[]],
		'usersActivityContinuos': [[],[],[],[]],
		'usersInteraction': [],
	}
	children = 0
	for group in groups:
		data['d3']['children'].append(group['d3'])
		group_name = group['d3']['name']
		group_speak_time = float(group['usersTime'][0]['y'])+float(group['usersTime'][1]['y'])+float(group['usersTime'][2]['y'])+float(group['usersTime'][3]['y'])
		data['groupsSpeakTime'].append({'x':group_name,'y':'{0:.2f}'.format(group_speak_time)})
		data['treemap_intdur']['children'].append({'name':group_name, 'children':[]})
		data['treemap_intdur']['children'][-1]['children'].append({'name':'Duración Intervención', 'children': []})
		data['treemap_volume']['children'].append({'name':group_name, 'children':[]})	
		data['treemap_volume']['children'][-1]['children'].append({'name':'Volumen', 'children': []})
		data['treemap_interv']['children'].append({'name':group_name, 'children':[]})	
		data['treemap_interv']['children'][-1]['children'].append({'name':'Intervención', 'children': []})
		user_pos = 1
		intdur_sum = 0
		interv_sum = 0
		induruser_sum = 0
		volsum = 0
		for i in range(len(group['usersIntDur'])):
			for intdur in group['usersIntDur'][i]:
					induruser_sum += float(intdur['y'])
			intdur_sum += induruser_sum
			interv_sum += len(group['usersIntDur'][i])
			data['treemap_intdur']['children'][-1]['children'][-1]['children'].append({'name':group_name+group['usersVolAVG'][i]['x']+'Duración: '+'{0:.2f}'.format(induruser_sum), 'size':'{0:.2f}'.format(induruser_sum)})
			data['treemap_volume']['children'][-1]['children'][-1]['children'].append({'name':group_name+group['usersVolAVG'][i]['x']+'Intensidad: '+group['usersVolAVG'][i]['y'], 'size':'{0:.2f}'.format(float(group['usersVolAVG'][i]['y']))})
			data['treemap_interv']['children'][-1]['children'][-1]['children'].append({'name':group_name+group['usersVolAVG'][i]['x']+'Intervenciones: '+str(len(group['usersIntDur'][i])), 'size':'{0:.2f}'.format(induruser_sum)})
			user_pos += 1
			volsum += float(group['usersVolAVG'][i]['y'])
		volavg = volsum / 4
		data['groupsIntervTime'].append({'x':group_name, 'y':'{0:.2f}'.format(intdur_sum)})
		data['groupsInterv'].append({'x':group_name, 'y':str(interv_sum)})
		data['groupsVolume'].append({'x':group_name, 'y':'{0:.2f}'.format(volavg)})
	return data