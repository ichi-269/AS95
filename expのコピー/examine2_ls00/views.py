from django.shortcuts import render
# Create your views here.

def index(request):
    try:
        return render(request,'examine2_ls00.html')
    except Exception as e:
        print(e)