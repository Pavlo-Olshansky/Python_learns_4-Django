from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'my_content': ['If you would to contact me, send an email ', 'pavlo.olshansky@gmail.com']})
