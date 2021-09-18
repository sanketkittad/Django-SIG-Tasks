from django.urls import path,include
from . import views
urlpatterns=[
    path('todo/',views.todo,name="todo"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('complete/<int:id>',views.complete,name="complete"),
]