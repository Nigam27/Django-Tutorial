from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    current_time = datetime.now()
    post = {
        "title": "My Second Templates Post",
        "description": "This is my second post using templates in Django.",
        "author": "None",
        "created_at":datetime(2026, 8, 19, 10, 30),
        "comments_count": 5,
        "tags": ["Python", "Django", "web development"],
        "price": 100,
        "Number": 10,
        'current_time': current_time
    }
    return render(request, 'blog/blog_details.html',{"post": post})

# Create your views here. 
