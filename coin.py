# -*- coding: utf-8 -*-
import requests
import json
import csv
import os
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def fetch_cryptocompare():
	coins = {'BTC','ETH', 'XRP'} # 가격정보를 원하는 코인 종류/ Set
	exchanges = {'Coinone':'KRW', 'Bithumb':'KRW', 'Bitfinex':'USD'} # 정보를 받아올 시장 / Dictionary
	_dict = {}
	cur = datetime.datetime.now() # 날짜를 저장
	timestamp = cur.strftime('%Y-%m-%d-%H:%M')
	_dict["Time"] = timestamp

	for market,currency in exchanges.items():
		#Cyptocompare API/ request information on the coin, currency and market
		url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=%s&tsyms=%s&e=%s' % (','.join(coins), currency, market)
		response = requests.get(url)
		data = response.json() #get the response and convert to json

		for coin in coins: # _dict에 해당 가격정보 저장
			if response.status_code == requests.codes.ok:
				#data['ETH']['KRW'], 소수점2자리
				_dict[market+'-'+coin+'-'+currency] = format(float(data[coin][currency]), ',f')[0:-4] 
			else:
				_dict[market+'-'+coin+'-'+currency] = -1 #if request is not ok, store -1


	with open(r'coin.csv', 'w') as f: # _dict에 저장된 정보를 coin.csv파일에 저장.
		writer = csv.writer(f)
		for key, value in _dict.items():
			writer.writerow([key, value])
	print("Success") #코드가 잘 돌고있는지 확인

def scheduler():
    sched = BlockingScheduler()
    sched.configure(timezone='Asia/Seoul')
    sched.add_job(fetch_cryptocompare, 'interval', minutes=1) #매 분마다 돌리기
    sched.start()



scheduler() #START!!!
