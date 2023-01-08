# pages/urls.py
from django.urls import path
#from .views import homePageView
from .views import HomePageView, AboutPageView

# urlpatterns = [
#    path("", homePageView, name="home"),
#]

urlpatterns = [
    path("home.html", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about")
]