from django.shortcuts import render

# Create your views here.
def info(request):
    students = ['지수', '준영', '진희']
    context = {
        'students': students,
        'teacher': '타키쌤'
    }
    return render(request, 'info.html', context)

def student(request, name):
    student = {
        '지수': 28,
        '준영': 26,
        '진희': 20
    }
    context = {
        'name': name,
        'age': student[name]
    }
    return render(request, 'student.html', context)

def one(request):
    return render(request, 'one.html')

def two(request):
    return render(request, 'two.html')