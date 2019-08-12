# 표준 라이브러리는 위에 써주는 것이 좋음!
import random
import datetime

from django.shortcuts import render

# Create your views here.

# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)


def lotto(request):
    print(request)
    print(type(request))
    print(request.META)
    # 로직
    numbers = sorted(random.sample(range(1, 46), 6))
    # 값을 딕셔너리에 담아서 (보통 context라고 부름)
    context = {'numbers': numbers}
    # render 함수의 필수 인자 : request, template 파일
    # 변수를 넘겨주고 싶으면 3번째 인자로 dictionary를 넘겨준다.
    # Django에서 활용하는 템플릿 언어는 Django Template Language(DTL)!
    return render(request, 'lotto.html', context)


def dinner(request):
    menus = ['롯데리아', '편의점 도시락', '맘스터치', '응급실떡볶이', '노은각', '피자', '치킨']
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'menus': menus,
        'users': [],
        'sentence': 'Life is short, You need Python + Django',
        'datetime_now': datetime.datetime.now(),
        'google_link': 'https://www.google.com'
    }
    return render(request, 'dinner.html', context)

# 인자에 들어가는 변수는 urls.py에서 정의한 이름과 같아야함!
def cube(request, number):
    result = number**3
    context = {
        'result': result,
        'number': number,
        'numbers': [1, 2, 3],
        'students': {'지수': '지수!'}
    }
    return render(request, 'cube.html', context)

def about(request, name, age):
    context = {
        'name': name,
        'age': age
    }
    return render(request, 'about.html', context)