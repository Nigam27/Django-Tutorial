from django.shortcuts import render
from datetime import datetime

# Create your views here.
def blog_details(request):
    current_time = datetime.now()
    blog = [
        {'title': 'Django Basics', 'is_featured':True, 'author':'Nigam Kumar'},
        {'title': 'Django Advanced', 'is_featured':False, 'author':'Ayush Kumar'},
        {'title': 'Django Rest Framework', 'is_featured':False, 'author':'sunami Kumari'}
    ]
    context = {
        'current_time': current_time,
        'blog': blog,
        'today': current_time.date(),
        'html_code': '<h1>Welcome to My Blog </h1>',
    }
    return render(request, 'blog/blog_details.html', context)
