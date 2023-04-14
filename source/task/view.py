from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_view(request):
    try:
        answer = json.loads(request.body)
        a = int(answer.get('A'))
        b = int(answer.get('B'))
        answer_as_json = a + b
        return JsonResponse({'answer': answer_as_json})
    except ValueError:
        response = JsonResponse({'error': 'A string value has been entered!'})
        response.status_code = 400
        return response


@csrf_exempt
def subtract_view(request):
    try:
        answer = json.loads(request.body)
        a = int(answer.get('A'))
        b = int(answer.get('B'))
        answer_as_json = a - b
        return JsonResponse({'answer': answer_as_json})
    except ValueError:
        response = JsonResponse({'error': 'A string value has been entered!'})
        response.status_code = 400
        return response


@csrf_exempt
def multiply_view(request):
    try:
        answer = json.loads(request.body)
        a = int(answer.get('A'))
        b = int(answer.get('B'))
        answer_as_json = a * b
        return JsonResponse({'answer': answer_as_json})
    except ValueError:
        response = JsonResponse({'error': 'A string value has been entered!'})
        response.status_code = 400
        return response


@csrf_exempt
def divide_view(request):
    try:
        answer = json.loads(request.body)
        a = int(answer.get('A'))
        b = int(answer.get('B'))
        answer_as_json = a / b
        return JsonResponse({'answer': answer_as_json})
    except ZeroDivisionError:
        response = JsonResponse({'error': 'Division by zero!'})
        response.status_code = 400
        return response
    except ValueError:
        response = JsonResponse({'error': 'A string value has been entered!'})
        response.status_code = 400
        return response
