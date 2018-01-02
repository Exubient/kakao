
import requests
import json
import csv
import os
import datetime

def fetch_cryptocompare():
	coins = {'BTC','ETH'}
	exchanges = {'Coinone':'KRW', 'Bithumb':'KRW', 'Korbit':'KRW', 'Bitfinex':'USD' }
	_dict = {}
	timestamp = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')
	for market,currency in exchanges.items():
        	url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=%s&tsyms=%s&e=%s' % (','.join(coins), currency, market)
       		response = requests.get (url)
        	data = response.json()

        	for c in coins:
        		if response.status_code == requests.codes.ok:
        	        	_dict[market+'-'+c+'-'+currency] = data[c][currency] #data['ETH']['KRW']
			else:
				_dict[market+'-'+c+'-'+currency] = -1
	cur = datetime.datetime.now()
	timestamp = cur.strftime('%Y-%m-%d-%H:%M')
	alias = _dict.keys(); alias.insert(0,'Date')
	data = _dict.values(); data.insert(0,timestamp)
	print(cur)
	print(timestamp)
	print(alias)
	print(data)	

def save():
	with open(r'coin.csv', 'r') as f:
        	lastrow = None
        	for lastrow in csv.reader(f):
               		pass

fetch_cryptocompare()
#date = datetime.datetime.now()
#result_date = "%s-%s-%s %s:%s" % (date.year, date.month, date.day, date.hour, date.minute)
#_fields=['DATE','Bitfinex-BTC-USD','Bithumb-BTC-KRW']
# index 3 and 4 shows the profit of BTC from finix and bitthumb seperately in dollars and won
#fields=[result_date, finix["USD"], thumb["KRW"]]

#with open(r'coin.csv', 'a') as f:
#        writer = csv.writer(f)
#        writer.writerow(fields)

#################crontab -l on linux EC2##################
#* * * * * /usr/bin/python3 /home/ubuntu/coin-2013012405.py


