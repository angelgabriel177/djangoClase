from django.urls import path
from.views import HomePageVierw
from.views import AboutPageVierw
urlpatterns = [
    path("", HomePageVierw.as_view(), name = "home"),
    path("about/", AboutPageVierw.as_view(), name ="about")
]