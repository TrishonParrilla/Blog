from django.urls import path
from .views import (HomePageView)
from .views import (AboutPageView)
from .views import (contact_me)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"), 
    path("contact/", contact_me, name="contact"), #because it is a function and not a class we dont need to pass a function
]