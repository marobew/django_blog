from django.shortcuts import render

# model view template(index.html)

def home(request):
    return render(request, 'post/index.html')