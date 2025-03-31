from django.urls import path

from . import views

urlpatterns = [
    path("hi/", views.hello_world, name="Hi"),
    path("", views.render_page, name="HTML Home page")

]
