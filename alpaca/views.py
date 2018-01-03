from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request):
	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['Coinone', 'Bithumb', 'Bitfinex']
		})

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    market = received_json_data['content']
    

    return JsonResponse({
            'message': {
                'text': market
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['Coinone', 'Bithumb', 'Bitfinex']
            }

        })


