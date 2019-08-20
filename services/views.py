import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    response = requests.get(url).text
    context = {
        'response': response
    }
    return render(request, 'services/artii_result.html', context)

def push(request):
    return render(request, 'services/push.html')

def pull(request):
    num = request.GET.get('num')
    context = {
        'num': num
    }
    return render(request, 'services/pull.html', context)