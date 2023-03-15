from django.urls import path

from . import views

urlpatterns =[
    path('create_group/',views.create, name="create_group"),
]

