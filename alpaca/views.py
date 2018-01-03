from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime, csv

def keyboard(request):
	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['Coinone', 'Bithumb', 'Bitfinex']
		})
@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    returnButton = received_json_data['content']
    with open(r'coin.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            info = row[0].split("-")
            ret = info[0]
            if info[0] == returnButton:
                return JsonResponse({
                    'message': {
                        'text': "you have selected " + returnButton
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['BTC', 'ETH', 'XRP']
                    }

                })
            if info[1] == returnButton and ret == info[0]: 
                ret = ""
                return JsonResponse({
                    'message': {
                        'text': row[1]
                     },
                    'keyboard':{
                        'type': 'buttons',
                        'buttons' : ['Coinone', 'Bithumb', 'Bitfinex']

                        }
                })


