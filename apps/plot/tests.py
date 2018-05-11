from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
import os
# Create your tests here. 
class GenerateVisualization(TestCase):

	def upload_file(self):
		c = Client()
		file = os.path.abspath("./apps/plot/test/file.csv")
		with open(file) as fp:
			self.response = c.post(reverse('upload_file'), {'csv_file': fp})

	def test_upload_file(self):
		self.upload_file()
		#status 302 redirect
		if(self.response.status_code==302):
			print("El servidor ha respondido correctamente con codigo:",  self.response.status_code)
		self.assertRedirects(self.response,reverse('plot'),302)

	def test_visualization(self):
		c = Client()
		self.upload_file()		
		response = c.get(reverse('plot'))
		if(response.status_code==200):
			print("El servidor ha respondido correctamente con codigo:", response.status_code)
		#status 200 OK 
		self.assertEquals(response.status_code, 200)


			