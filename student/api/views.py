from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
 
 
def index(request):
    response = {
        'id': 1,
        'name': 'Tom',
        'status': "Active"
    }
    return JsonResponse(response)
 