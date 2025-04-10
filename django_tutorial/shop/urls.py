from django.urls import path

from . import views

urlpatterns = [
    path("hi/", views.hello_world, name="Hi"),
    path("", views.render_page, name="home_page"),
    path("about/", views.about, name="about")

]
