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

	def grabAccessToken(self, user, code, save=True):
		code = code.replace(" ", "");

		raw = self.callAPIPost("api/v2/oauth/token", {"grant_type": "authorization_code", "code": "88888888888"});

		print(raw);



	def getToken(self, id):
		# Check if cache file does exists

		if os.path.isfile('cache.json') is True:
			filereader = open('cache.json', 'r');

			data = json.loads(filereader.readline());

			if str(id) in data:
				return data[str(id)];
			else:
				return None;


	def saveToken(self, id, token):

		current = [];
		
		# Check for an existing cache file
		if os.path.isfile('cache.json') is True:
			filereader = open('cache.json', 'r');

			current = json.loads(filereader.readline());
			filereader.close();

		current['tokens'][str(user)] = token;

		jsonraw = json.dumps(current['tokens']);

		# Clear the old cache file
		open('cache.json', 'w').close()

		# Write the new cache file
		filewriter = open('cache.json', 'w');
		filewriter.write(jsonraw);

		filewriter.close()



	def callAPI(self, uri, payload=[]):
		# Receive the base url

		baseurl = self.getBaseURL();

		# Creating a request

		request = requests.get(baseurl, params=payload);
		return request.url;

	def callAPIPost(self, uri, payload):
		# Receive the base url

		baseurl = self.getBaseURL(uri);

		# Creating a request

		request = requests.post(baseurl, payload, verify=False);
		return request.text;

	def getBaseURL(self, uri=""):
		return "https://" + self.school + ".zportal.nl/" + uri;


