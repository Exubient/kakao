from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

def keyboard(request):
	return JsonResponse({
		'type' : 'buttons',
		'buttons' : ['B1', 'B2', 'B3']
		})

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    return_str = received_json_data['content']

    requestMode = return_str.encode('utf-8')  # utf-8형식으로 인코딩하여 한글을 인식

    if requestMode == "B1":
        return JsonResponse({
                'message': {
                    'text': 'test worked'
                },
                'keyboard': {
                    'type': 'buttons',
                }

            })


