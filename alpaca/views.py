from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime, csv, ast

ret ={}
def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['Coinone', 'Bithumb', 'Bitfinex'] #Kakao default API 테스트용
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
                        'text': "you have selected " + returnButton #첫번째 버튼set
                     },
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': ['BTC', 'ETH', 'XRP'] #response다음으로 보일 버튼
                    }

                })
                
            if(returnButton == info[1] and ret[_dict["user_key"]] == info[0]): #ret에 저장된 시장과 가상화폐에 해당되는 가격 출력
                return JsonResponse({
                    'message': {
                        'text': row[1] + info[2] #출력
                     },
                    'keyboard':{
                        'type': 'buttons',
                        'buttons' : ['Coinone', 'Bithumb', 'Bitfinex'] #response다음으로 보일 버튼

                        }
                })


