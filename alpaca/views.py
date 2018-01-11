from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime, csv, ast

ret ={}
def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['Coinone', 'Bithumb', 'Bitfinex'] #buttons shown at first, default API test
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
            info = row[0].split("-") #info[0] 시장, info[1]가상화폐 종류, info[2] 단위
            if(returnButton == info[0]):  # 첫번째로 보일 키보드, 시장을 선택 했을때 True
                global ret #Database에 저장해야 되지만 세미나 특성상 state를 이렇게 처리합니다
                ret[_dict["user_key"]] = info[0] #방금 유저가 어떤 시장을 눌렀을지 저장
                return JsonResponse({
                    'message': {
                        'text': "you have selected " + returnButton #first response from button
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['BTC', 'ETH', 'XRP'] #buttons shown after first response
                    }

                })
                
            if(returnButton == info[1] and ret[_dict["user_key"]] == info[0]): #find the cell that contains the market user has pressed on ret
                return JsonResponse({
                    'message': {
                        'text': row[1] + info[2] #second response from button
                     },
                    'keyboard':{
                        'type': 'buttons',
                        'buttons' : ['Coinone', 'Bithumb', 'Bitfinex'] #set of buttons shown after second response

                        }
                })


