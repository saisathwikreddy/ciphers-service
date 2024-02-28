from django.http import JsonResponse
from .ciphers import caesar_encode

def greetings(request):
    return JsonResponse({"message": "Welcome to the Ciphers server!"})

def encode (request, plaintext, shift):
    parameters = dict (request.GET)
    print (parameters)
    cipher = caesar_encode (plaintext, shift)
    return JsonResponse({"cipher": cipher})