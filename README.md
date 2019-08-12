# Django

* 장고? python의 가장 유명한 프레임워크
* Opinionated 다소 독선적!
  * MVC가 아닌 MTV
* "프레임워크를 쓴다."  => 약속을 지킨다.
  * 정해진 규칙대로 써야 원하는 결과를 얻을 수 있음.
  * 자유분방함이 적음
  * 프레임워크 배우는 이유 ? 정해진 스펙 아래서(프레임워크, 개발환경 등)에서 어떻게 배워야하는지 알 수 있다.
* cf. Framework : 완성된 소스 코드의 집합
* cf. Library : bootstrap같은
* [Hot Framework Rank](https://hotframeworks.com/)
* 지금까지 우리는 Static Web을 했다. 이제부터는 장고를 하면서 Dynamic Web을 할 것이다. 파이썬이 웹서버 구동.
* 웹서비스 제작 방법 
  1. A-Z 직접 다 하기
  2. Framework 사용



## Web Service

들어오는 요청 어떻게 응답할지 서버에서 정의.

기존 : html파일 만들어서 해당하는 html 파일을 보내주는 형식

Django: MTV(모델-DB, 사용자가 보는 화면-템플릿, view-중간 관리자) 요청이 들어오면 장고안에서 뷰가 먼저 받아서 요청이 들어온 것 캐치 후 모델에게 강의를 찾아달라함녀 db에서 찾아 view에게 전달, view는 template에게 사용자에게 보여달라고 요청.

### Template & View

가상환경을 독립적으로 사용 : 이유는 특정한 환경에서는 장고버전을 2.1을 쓸 수도 있고, 다양한 버전을 쓸 수도 있다. 그런 경우 pip 새로 깔지 않고 충돌 일어나지 않게 함.

```bash
가상환경 만들기
$ python -m venv venv

폴더 생성 확인할 수 있음
$ ll
drwxr-xr-x 1 student 197121    0  8월 12 10:40 venv/

$ git init

$ vi .gitignore
(3.7.4)
.gitignore에 venv/ 추가

가상환경 실행
$ source venv/Scripts/activate
(venv)

pip 업그레이드
python -m pip install --upgrade pip

설치
$ pip install django
------------------------------------------------------------------
만약 error 가 난다면
error
PermissionError: [WinError 5] 액세스가 거부되었습니다: 'c:\\program files\\python35\\Lib\\site-packages\\sqlparse'

(venv)
$ deactivate
$ venv
(3.7.4)
--> 일단 이렇게 하자.

$ pip install django
```

```bash
 장고 프로젝트 시작
 $ django-admin startproject first_django .
 
 
 $ python manage.py runserver
 
 웹브라우저에서 http://localhost:8000/
 
 
```

## 1. 시작하기

```bash
$ pip install django
```

* 현재 활용하고 있는 버전은 다음과 같다.
  * python 3.7.4
  * django 2.2.4

### 1. Django 프로젝트 시작

```bash
$ mkdir __프로젝트 이름/폴더 이름__
$ cd __프로젝트 이름/폴더 이름__
```

```bash
$ django-admin startproject __프로젝트이름__ .
```

* 프로젝트이름으로 구성도니 폴더와, `manage.py`가 생성된다.
  * `__init__.py` : 해당 폴더가 패키지로 인식될 수 있게끔 작성되는 파일
  * `settings.py` : **django 설정과 관련된 파일**
  * `urls.py` : **url 관리 **
  * `wsgi.py` : 배포시 사용(web server gateway interface : 파이썬에서 사용되는 웹 서버 구성)
  * `manage.py` : **django 프로젝트와 관련된 커맨드라인(명령어) 유틸리티**

### 2. 서버 실행

```bash
$ python manage.py runserver
```

* `localhost:8000`으로 들어가서 로켓 확인!



### manage.py

```bash
$ python manage.py startapp pages
```

pages라는 app을 만듬

* 여기서 app이란?
  * 예를 들어 페이스북에서 accounts, groups, posts,...로 관리한다 할때 이것들 모두가 app이라고 불림.



1. urls.py url 정의
2. views.py 함수정의
3. templates/__.html 템플릿 정의



### 3. App 생성

```bash
$ python manage.py startapp __app이름__
```

* `app이름`인 폴더가 생성되며, 구성하고 있는 파일은 다음과 같다.

  * `admin.py` : 관리자 페이지 설정

  * `apps.py` : app의 정보 설정. 직접 수정하는 경우 별로 없음.

  * `models.py` : **MTV-Model을 정의하는 곳**

  * `tests.py` : 테스트 코드를 작성하는 곳

  * `views.py` : **MTV-View를 정의하는 곳**

    * 사용자에게 요청이 왔을 때, 처리되는 함수

      ```python
      def index(request):
          return render(request, index.html)
      ```

**app을 만들고 나서 반드시 `settings.py`에서 `INSTALLED_APPS`에 app을 등록한다.**

```python
# first_django/settings.py
#..
INSTALLED_APPS = {
    'pages',
    'django.contrib.admin',
    # ...
]
}
#..
```



## 2. 작성 흐름

### 1. URL 정의

```python
# first_django/urls.py
from pages import views

urlpatterns = [
    path('', views.index), # => trailing comma 주의!
]
```

* `urls.py`는 우리의 앱 어플리케이션 경로들을 모두 관리한다.
* 요청이 들어오면 `urls.py`의 `urlpatterns`에 정의된 경로로 매핑한다.
* path(`경로`, `views에 정의된 함수`)

### 2. View 정의

```python
# pages/views.py

def index(request):
    return render(request, 'index.html')
```

* `views.py`는 MTV에서 View에 해당한다.
* 일종의 중간관리자로 Model, Template 등의 처리를 담당한다.
* (실질적으로 요청을 처리하는 역할)

### 3. Template 정의

* 기본적으로 app을 생성하면, `templates` 폴더가 없으므로 직접 생성해야 한다.

```html
<!-- pages/templates/index.html -->
<h1>
    장고, 안녕!
</h1>
```

### 4. 서버 실행 및 확인

```bash
$ python manage.py runserver
```

`localhost:8000`에서 확인해보자!

