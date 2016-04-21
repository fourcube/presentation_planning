from django.shortcuts import render

# Create your views here.


def new(request):
    context = {
        'content': 'Hello World!',
        'title': 'Test',
    }
    return render(request, 'create/new.html', context)
