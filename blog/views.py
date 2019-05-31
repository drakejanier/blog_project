from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Core',
        'title': 'Blog',
        'content': 'First post',
        'date_posted': 'aug 27, 2018'
    },
    {
        'author': 'Jer',
        'title': 'BALAG',
        'content': '2ND post',
        'date_posted': 'aug 28, 2018'
    }
]
def home(request):
    context = {
        'posts':posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})





