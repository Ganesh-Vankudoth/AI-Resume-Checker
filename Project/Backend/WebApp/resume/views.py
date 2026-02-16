from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def display(request):
    return JsonResponse({"message":"Resume app running successfully "})