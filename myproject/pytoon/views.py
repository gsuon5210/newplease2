from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['angry', 'fucking', 'hate']
    })
