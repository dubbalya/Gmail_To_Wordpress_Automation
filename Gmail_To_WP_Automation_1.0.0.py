#!/usr/local/bin/python3

import requests
import os
import json
import os.path
import pathlib
import base64
import datetime
import schedule

import ezgmail

class emailToWP():
	"""This simple automation utilizes Al Sweigart's ezgmail module and the Wordpress REST API
	to automate new blog posts. This class allows users to email a gmail address, read the email contents,
	download the image provided (limited to one per email), and upload the Subject, Email Contents,
	and Image as a new WP post."""

	def __init__(self, path=r'@INSERT YOUR OWN DEFAULT PATH@',
		url='https://YOURWEBSITE.com/wp-json/wp/v2', user='YOURUSERNAME',
		password='DO NOT STORE PASSWORD IN PRODUCTION CODE', # Use Application Passwords Plug-in to generate Key. Store in Environment Variables.
		User_Agent=f'INSERT YOUR OWN USER AGENT'):
		self.path = path
		self.messages = None
		self.url = url
		self.creds = user + ':' + password
		self.token = base64.b64encode(self.creds.encode())
		self.header = {'Authorization': 'Basic ' + self.token.decode('utf-8'), 'User-Agent': User_Agent}
		self.now = datetime.datetime.now()
		self.timestamp = datetime.date(self.now.year, self.now.month, self.now.day).isoformat()
		self.email1 = None
		self.email2 = None
		self.email3 = None

	def log_into_email(self):
		os.chdir(self.path)
		ezgmail.init()
		
	def access_new_messages(self):
		self.messages = ezgmail.unread()
		return self.messages

	def upload_contents(self, email1='', email2='', email3=''):
		"""Filter based on sender, perform download/upload actions,
		and mark email as read once complete. Content is limited to 200 or
		fewer characters for post (GmailMessage snippet attribute)."""

		self.email1 = email1
		self.email2 = email2
		self.email3 = email3
		for message in self.messages:
			if self.email1 in message.messages[0].sender or self.email2 in message.messages[0].sender or self.email3 in message.messages[0].sender:
				subject = message.messages[0].subject
				description = message.messages[0].snippet
				image = ''.join(message.messages[0].attachments)
				message.messages[0].downloadAttachment(image)

				media = {
					'file': open(image, 'rb'),
					'caption': image,
					'description': image,
				}

				image_response = requests.post(self.url + '/media', headers=self.header, files=media)
				image_id = image_response.json()['id']

				# Update below timezone as desired.

				post = {
					'date': f'{self.timestamp}T09:00:00',
					'title': subject,
					'content': description,
					'featured_media': image_id,
					'status': 'publish'
				}

				r = requests.post(self.url + '/posts', headers=self.header, json=post)
				message.messages[0].markAsRead()
			else:
				pass

	def upload_images_only(self, email1='', email2='', email3=''):
		"""Optional method to upload only images contained within the email"""
		self.email1 = email1
		self.email2 = email2
		self.email3 = email3
		for message in self.messages:
			if self.email1 in message.messages[0].sender or self.email2 in message.messages[0].sender or self.email3 in message.messages[0].sender:
				for image in message.messages[0].attachments:
					message.messages[0].downloadAttachment(image)

					media = {
						'file': open(image, 'rb'),
						'caption': image,
						'description': image,
					}

					image_response = requests.post(self.url + '/media', headers=self.header, files=media)
					image_id = image_response.json()['id']

					message.messages[0].markAsRead()
			else:
				pass						

def post_new_paintings():
	"""Execution of the above"""

	upload = emailToWP()
	upload.log_into_email()
	upload.access_new_messages()
	# Optional directory changes if images will be saved in separate folder.
	os.chdir(r'PATHTOREDIRECTIFNECESSARY')
	upload.upload_contents(email1='INSERTSENDEREMAIL@EMAIL.com')
	print('this is a test')

# Defaulted to 30 minute sweeps for new messages. Update as desired.

schedule.every(30).minutes.do(post_new_paintings)

while True:
    schedule.run_pending()