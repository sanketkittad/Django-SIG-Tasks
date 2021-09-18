from django.urls import path
from . import views
urlpatterns=[
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("index/",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("search/",views.search,name="search")
]