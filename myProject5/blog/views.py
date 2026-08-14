from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def home(request):
    context = {
        "name": "Nigam Kumar",
        "age": 22,
        "skills": ["Python", "Django", "React"],
        "user": User("Nigam", 22),
        "blog":{
            "title": "Django Template Intro",
            "author":{
                "name": " Nigam Kumar",
                "email": " nigam8032212gmail.com"
            },
            "content": "<p>This is a simple introduction to Django templates.</p>",
            "created_at": datetime(2026,8,18,10,30,)
        },
        "empty_value": None,
    }
    return render(request, "blog/home.html", context)
    