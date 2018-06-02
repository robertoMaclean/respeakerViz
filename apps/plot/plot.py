import csv
import wave
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
from io import StringIO
import os
import apps.plot.functions as functions


class Plot(object):

	def __init__(self, file, outputPath='media/plot/'):
		self.__file = file
		self.__outputPath = os.path.abspath(outputPath)
		self.__activity = [[],[],[],[]] 			#Each user activity (without silence)
		self.__activityContinuos = [[],[],[],[]]  	#Each user activity (include silence)
		self.__time = 0                        		#Activity time
		self.__userTime = []						#Users speak time
		self.__speakTime = 0						#Speak time of activity
		#self.__relations = [0,0,0,0,0,0]			#Relations between users
		self.__usersInterv = []						#Each user intervention
		self.__userStartInt = [[],[]]				#User intervention start
		self.__volPromInterv = [[],[],[],[]]		#User volume AVG per intervention
		self.__usersVol = []						#User total volume AVG
		self.__usersVolFrame = [[],[],[],[]]
		self.__usersRelations = [0,0,0,0,0,0,0,0,0,0,0,0]				
		functions.ensureDir(outputPath)
		self.ExtractData()
		self.UsersSpeak()
		# self.UsersInteraction()
		self.SpeakTime()

	def GetTime(self):
		return self.__time

	def GetUserTime(self):
		return self.__userTime

	def GetSpeakTime(self):
		return self.__speakTime

	def GetUsersInterv(self):
		return self.__usersInterv

	def GetUserStartInt(self):
		return self.__userStartInt

	def GetUsersVol(self):				#volumen promedio total usuario
		return self.__usersVol

	def GetUsersVolPromInterv(self):  	#volumen promedio por intervencion
		return self.__volPromInterv

	def GetActivity(self):
		return self.__activity

	def GetActivityContinuos(self):
		return self.__activityContinuos

	def GetUsersRelations(self):
		return self.__usersRelations

	def GetUsersVolFrame(self):
		return self.__usersVolFrame

	def ExtractData(self):
		interTimes = [[],[],[],[]]
		timeActivity = []
		volProm = []
		lastPosition = -1
		silence = 0
		reader = csv.DictReader(self.__file, delimiter=";", lineterminator='\n')
		file = open(self.__outputPath+'relaciones.csv', 'w', newline="\n")
		fieldnames = ['Emisor','Receptor','Interacciones']
		writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
		writer.writeheader()
		#file.write('Usuario 1;Usuario 2;Cantidad relaciones\n')
		for row in reader:
			self.__usersVolFrame[int(row['direction'])].append((row['amplitude'],row['seconds']))
			if int(row['speak']):
				#print("direccion:", str(row['direction']))
				if int(row['direction']) != lastPosition:
					self.__userStartInt[0].append(int(row['direction'])+1)
					self.__userStartInt[1].append(float(row['seconds']))
					if lastPosition != -1:
						prom = sum(volProm)/len(volProm)
						self.__volPromInterv[lastPosition].append((prom,row['seconds']))
						volProm = []
						interTimes[lastPosition].append(timeActivity)
						#self.FindUsersInteraction(lastPosition+1, int(row['direction'])+1, file)
						self.FindUsersInteraction(lastPosition+1, int(row['direction'])+1, file)
						for i in range(silence):
							self.__activityContinuos[lastPosition].pop()
					else:
						for i in range(silence):
							self.__activityContinuos[0].pop()
					#self.__volPromInterv[lastPosition].append("{0:.2f}".format(sum(volProm)/len(volProm)))			
					timeActivity = []														
				self.__activity[int(row['direction'])].append(float(row['seconds']))
				volProm.append(float(row['amplitude']))							
				timeActivity.append(float(row['seconds']))
				lastPosition = int(row['direction'])
				silence = 0
			else:
				silence += 1
			self.__activityContinuos[int(row['direction'])].append(float(row['seconds']))	
			self.__time = row['seconds']
		file.close()
		interTimes[lastPosition].append(timeActivity)
		for i in range(silence):
			self.__activityContinuos[lastPosition].pop()
		for x in interTimes:
			self.__usersInterv.append(x)
		total_vol = 0
		for x in self.__volPromInterv:
			for prom, time in x: 
				total_vol += prom
			self.__usersVol.append(total_vol/len(x))

	def UsersSpeak(self):
		#figure = plt.gcf() # get current figure
		#figure.set_size_inches(12, 5, forward=True)
		plt.figure(figsize=(12, 4))
		plt.subplot(2,1,1)
		if(float(self.__time)<10):
			sep = 1
		else:
			sep = int(float(self.__time)/12)
		plt.xticks(np.arange(0, float(self.__time)+1, sep))
		plt.yticks([1],["Voz activa"])
		plt.vlines(self.__activity[0], 0, 1, label='Usuario 1', color='red')
		plt.vlines(self.__activity[1], 0, 1, label='Usuario 2', color='blue')
		plt.vlines(self.__activity[2], 0, 1, label='Usuario 3', color='green')
		plt.vlines(self.__activity[3], 0, 1, label='Usuario 4', color='orange')
		plt.xlabel("tiempo (segundos)") 
		plt.title("Activación de voz con silencios")
		plt.subplot(2,1,2)
		plt.xticks(np.arange(0, float(self.__time)+1, sep))
		plt.yticks([1],["Voz activa"])
		plt.vlines(self.__activityContinuos[0], 0, 1, label='Usuario 1', color='red')
		plt.vlines(self.__activityContinuos[1], 0, 1, label='Usuario 2', color='blue')
		plt.vlines(self.__activityContinuos[2], 0, 1, label='Usuario 3', color='green')
		plt.vlines(self.__activityContinuos[3], 0, 1, label='Usuario 4', color='orange')
		plt.xlabel("tiempo (segundos)") 
		plt.title("Activación de voz sin silencios")		
		leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.5), fancybox=False, shadow=False, 
				ncol=5)
		for line in leg.get_lines():
			line.set_linewidth(4.0)
		plt.tight_layout()
		plt.savefig(self.__outputPath+'users_speak.png')
		plt.close()

	# def FindUsersInteraction(self, pos1, pos2, file):
	# 		#writer.writeheader()
	# 		fieldnames = ['Usuario 1','Usuario 2','Relaciones']
	# 		writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
			
	# 		if pos1+pos2 == 3:
	# 			writer.writerow({'Usuario 1':str(pos1),'Usuario 2':str(pos2),'Relaciones':str(self.__relations[0]+1)})
	# 			self.__relations[0] += 1
	# 		elif pos1+pos2 == 4:
	# 			writer.writerow({'Usuario 1':str(pos1),'Usuario 2':str(pos2),'Relaciones':str(self.__relations[1]+1)})
	# 			self.__relations[1] += 1
	# 		elif pos1 == 1 or pos2 == 1:
	# 			writer.writerow({'Usuario 1':str(pos1),'Usuario 2':str(pos2),'Relaciones':str(self.__relations[2]+1)})
	# 			self.__relations[2] += 1
	# 		elif pos1 + pos2 == 5:
	# 			writer.writerow({'Usuario 1':str(pos1),'Usuario 2':str(pos2),'Relaciones':str(self.__relations[3]+1)})
	# 			self.__relations[3] += 1
	# 		elif pos1 + pos2 == 6:
	# 			writer.writerow({'Usuario 1':str(pos1),'Usuario 2':str(pos2),'Relaciones':str(self.__relations[4]+1)})
	# 			self.__relations[4] += 1
	# 		else:
	# 			writer.writerow({'Usuario 1':str(pos1),'Usuario 2':str(pos2),'Relaciones':str(self.__relations[5]+1)})
	# 			self.__relations[5] += 1

	def FindUsersInteraction(self, pos1, pos2, file):
		fieldnames = ['Emisor','Receptor','Interacciones']
		writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")

		if pos1==1 and pos2 == 2:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[0]+1)})
			self.__usersRelations[0] += 1
		elif pos1==1 and pos2 == 3:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[1]+1)})
			self.__usersRelations[1] += 1
		elif pos1==1 and pos2 == 4:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[2]+1)})
			self.__usersRelations[2] += 1
		elif pos1==2 and pos2 == 1:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[3]+1)})
			self.__usersRelations[3] += 1
		elif pos1==2 and pos2 == 3:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[4]+1)})
			self.__usersRelations[4] += 1
		elif pos1==2 and pos2 == 4:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[5]+1)})
			self.__usersRelations[5] += 1
		elif pos1==3 and pos2 == 1:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[6]+1)})
			self.__usersRelations[6] += 1
		elif pos1==3 and pos2 == 2:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[7]+1)})
			self.__usersRelations[7] += 1
		elif pos1==3 and pos2 == 4:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[8]+1)})
			self.__usersRelations[8] += 1
		elif pos1==4 and pos2 == 1:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[9]+1)})
			self.__usersRelations[9] += 1
		elif pos1==4 and pos2 == 2:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[10]+1)})
			self.__usersRelations[10] += 1
		elif pos1==4 and pos2 == 3:
			writer.writerow({'Emisor':str(pos1),'Receptor':str(pos2),'Interacciones':str(self.__usersRelations[11]+1)})
			self.__usersRelations[11] += 1

	# def UsersInteraction(self):
	# 	node_speak = []
	# 	pix_max = 1500
	# 	pix_min = 500
	# 	func_max = []
	# 	func_min = []
	# 	maximo = max([len(self.__activity[0]),len(self.__activity[1]),len(self.__activity[2]),len(self.__activity[3])])
	# 	for i in range(0, len(self.__activity)):
	# 		node_speak.append(len(self.__activity[i]))
	# 		func_max.append(int((float(len(self.__activity[i]))/maximo)*(pix_max-pix_min)+pix_min))

	# 	edgelist = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
	# 	G=nx.Graph(edgelist)
	# 	pos=nx.circular_layout(G)
	# 	nx.draw(G,pos,node_color='#A0CBE2',node_size=func_max, edge_color=self.__relations,width=4,edge_cmap=plt.cm.Blues,with_labels=True)
	# 	#plt.show()
	# 	plt.savefig(self.__outputPath+'users_interaction.png')
	# 	plt.close()

	def SpeakTime(self):
		suma = len(self.__activity[0])+len(self.__activity[1])+len(self.__activity[2])+len(self.__activity[3])
		self.__speakTime = suma*0.02
		self.__userTime.append("{0:.2f}".format(len(self.__activity[0])*0.02)) 
		self.__userTime.append("{0:.2f}".format(len(self.__activity[1])*0.02))
		self.__userTime.append("{0:.2f}".format(len(self.__activity[2])*0.02))
		self.__userTime.append("{0:.2f}".format(len(self.__activity[3])*0.02)) 
		