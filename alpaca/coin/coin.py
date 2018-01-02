
import requests
import json
import csv
import os
import datetime

def fetch_cryptocompare():
	coins = {'BTC','ETH'}
	exchanges = {'Coinone':'KRW', 'Bithumb':'KRW', 'Korbit':'KRW'}

	_dict = {}
	cur = datetime.datetime.now()
	timestamp = cur.strftime('%Y-%m-%d-%H:%M')
	_dict["Time"] = timestamp

	for market,currency in exchanges.items():
		url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=%s&tsyms=%s&e=%s' % (','.join(coins), currency, market)
		response = requests.get (url)
		data = response.json()

		for coin in coins:
			if response.status_code == requests.codes.ok:
				_dict[market+'-'+coin+'-'+currency] = data[coin][currency] #data['ETH']['KRW']
			else:
				_dict[market+'-'+coin+'-'+currency] = -1
	return _dict



ret = fetch_cryptocompare()
with open(r'coin.csv', 'w') as f:
	writer = csv.writer(f)
	for key, value in ret.items():
		writer.writerow([key, value])

################crontab -l on linux EC2##################
# * * * * * /usr/bin/python3 /home/ubuntu/coin-2013012405.py


