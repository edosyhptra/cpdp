from django.shortcuts import render

# Create your views here.
def view(request, id):
    context = {
        'id': id
    }
    return render(request, 'app_blog/read.html', context)