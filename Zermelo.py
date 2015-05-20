import time;
import datetime;
import requests;
import os.path;
import json;

class API:
	def __init__(self, school, secure=False):
		# Save variables to class storage

		self.school = school.lower();
		self.secure = secure;


	def getStudentGrid(self, id, start, end):
		# Set the start times if they are not set

		print(id);

	def saveToken(user, token):
		current = [];

		if os.path.isfile('cache.json') is True:
			file = open('cache.json', 'r');

			current.append(json.loads(file.readline()));
		
		current.append("{token : " + str(token) + "}");

		print(current);



	def callAPI(self, url, payload=[]):
		# Receive the base url

		baseurl = self.getBaseURL();

		# Creating a request

		request = requests.get(baseurl, params=payload);
		return request.url;

	def callAPIPost(self, url, payload=[]):
		# Receive the base url

		baseurl = self.getBaseURL();

		# Creating a request

		request = requests.post(baseurl, data=payload);
		return request.text;

	def getBaseURL(self, uri=""):
		return "https://" + self.school + ".zportal.nl/" + uri;


