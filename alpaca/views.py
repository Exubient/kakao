from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime, csv, ast

ret ={}
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
    _dict = ast.literal_eval(json_str)
    with open(r'coin.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            info = row[0].split("-")
            if(returnButton == info[0]):
                global ret
                ret[_dict["user_key"]] = info[0]
                return JsonResponse({
                    'message': {
                        'text': "you have selected " + returnButton
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['BTC', 'ETH', 'XRP']
                    }

                })
                
            if(returnButton == info[1] and ret[_dict["user_key"]] == info[0]):
                return JsonResponse({
                    'message': {
                        'text': row[1] + info[2]
                     },
                    'keyboard':{
                        'type': 'buttons',
                        'buttons' : ['Coinone', 'Bithumb', 'Bitfinex']

                        }
                })


