from django.shortcuts import render

posts = [
    {
        'author': 'Bailey',
        'title': 'Blog post 1',
        'content': 'Blah blah blah',
        'data_posted': 'January 29th, 2019'
    },
    {
        'author': 'Friend Guy',
        'title': 'Guy\'s post',
        'content': 'Blah blah blah',
        'data_posted': 'January 30th, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")
