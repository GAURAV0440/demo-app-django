from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='text-align: center; margin-top: 20%;'>Hello, welcome to my Django app!</h1>")
