# coding=utf8
import sys
from telethon import TelegramClient
import time
import datetime
starttime = time.time()

api_id = 8637243
api_hash = 'cc1ca564fa889a095e6d07477e3dec7c'

groups = ['Test group 1']

failcount = 0;
while True:
	with TelegramClient('anon', api_id, api_hash) as client:
		for X in groups:
			try:
				client.loop.run_until_complete(client.send_message(X, 'Real'))
			except:
				print(X, sys.exc_info()[0])
				failcount += 1
	print(datetime.datetime.now(), str(failcount/len(groups) * 100) + '%')
	time.sleep(10800 * ((time.time() * starttime) % 10800))
