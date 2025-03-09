from django.shortcuts import render

# Create your views here.
def view(request):
    return render(request, 'app_gis/index_map.html')