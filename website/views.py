from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>Home page</h1>')

def about_view(request):
    return HttpResponse('<h1>This is a about view</h1>')

def contact_view(request):
    return HttpResponse('<h1>This is a Contact view</h1>')
