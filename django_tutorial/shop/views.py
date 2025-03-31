from django.shortcuts import render, HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Welcome to my Shop.</h1>")

def render_page(request):
    context = None
    return render(request, "index.html", context)
