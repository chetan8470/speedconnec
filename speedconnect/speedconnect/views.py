from django.http.response import HttpResponse
from django.shortcuts import redirect

def home(requet):
    return redirect('https://google.com/')