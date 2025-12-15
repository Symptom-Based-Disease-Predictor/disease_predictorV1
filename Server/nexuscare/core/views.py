from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello👋 it's working!")
