import csv
import wave
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import networkx as nx
from io import StringIO
from django.conf import settings as djangoSettings
import os
import apps.plot.functions as functions


class Plot(object):

	def __init__(self, file, outputPath='media/plot/'):
		self.__file = StringIO(file)
		self.__outputPath = os.path.abspath(outputPath)
		self.__activity = [[],[],[],[]]
		self.__time = 0
		self.__userTime = [4]
		self.__relations = [0,0,0,0,0,0]
		functions.ensureDir(outputPath)
		self.ExtractData()

	def ExtractData(self):
		interTimes = [[],[],[],[]]
		timeActivity = []
		lastPosition = -1
		print(self.__outputPath)
		reader = csv.DictReader(self.__file, delimiter=";")
		for row in reader:
			if int(row['speak']):
				if int(row['direction']) != lastPosition:
					if lastPosition != -1:
						interTimes[lastPosition].append(timeActivity)
						timeActivity = []
						self.FindUsersInteraction(lastPosition+1, int(row['direction'])+1)
				timeActivity.append(float(row['seconds']))
				lastPosition = int(row['direction'])
				self.__activity[lastPosition].append(float(row['seconds']))
			self.__time = row['seconds']

	def UsersSpeak(self):
		figure = plt.gcf() # get current figure
		figure.set_size_inches(12, 4, forward=True)
		plt.subplot(3,1,1)
		plt.xticks(np.arange(0, float(self.__time)+1, 10))
		plt.yticks([1],["Voz activa"])
		plt.vlines(self.__activity[0], 0, 1, linewidth=0.05, label='Usuario 1', color='red')
		plt.vlines(self.__activity[1], 0, 1, linewidth=0.05, label='Usuario 2', color='blue')
		plt.vlines(self.__activity[2], 0, 1, linewidth=0.05, label='Usuario 3', color='green')
		plt.vlines(self.__activity[3], 0, 1, linewidth=0.05, label='Usuario 4', color='orange')
		plt.xlabel('tiempo (segundos)') 
		#plt.legend(frameon=True, framealpha=0.6)
		leg = plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.5), fancybox=False, shadow=False, 
				ncol=5)
		for line in leg.get_lines():
			line.set_linewidth(4.0)
		plt.savefig(self.__outputPath+'users_speak.png', dpi=1200)
		#plt.show()
		plt.close(figure)

	def FindUsersInteraction(self, pos1, pos2):
		if pos1+pos2 == 3:
			self.__relations[0] += 1
		elif pos1+pos2 == 4:
			self.__relations[1] += 1
		elif (pos1 or pos2) == 1:
			self.__relations[2] += 1
		elif pos1 + pos2 == 5:
			self.__relations[3] += 1
		elif pos1 + pos2 == 6:
			self.__relations[4] += 1
		else:
			self.__relations[5] += 1

	def UsersInteraction(self):
		edgelist = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
		G=nx.Graph(edgelist)
		pos=nx.circular_layout(G)
		nx.draw(G,pos,node_color='#A0CBE2',edge_color=self.__relations,width=4,edge_cmap=plt.cm.Blues,with_labels=True)
		#plt.show()
		plt.savefig(self.__outputPath+'/users_interaction.png')

	def SpeakTime(self):
		suma = len(self.__activity[0])+len(self.__activity[1])+len(self.__activity[2])+len(self.__activity[3])
		print(suma*0.02)
		print(len(self.__activity[0])*0.02)
		print(len(self.__activity[1])*0.02)
		print(len(self.__activity[2])*0.02)
		print(len(self.__activity[3])*0.02)