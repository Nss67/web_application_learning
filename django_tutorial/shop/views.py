from django.shortcuts import render, HttpResponse

from . import models

def hello_world(request):
    return HttpResponse("<h1>Welcome to my Shop.</h1>")

def render_page(request):
    # query set
    all_products = models.Products.objects.all()
    # for send and combine all result to html file 
    context = {"products": all_products}

    return render(request, "index.html", context)
