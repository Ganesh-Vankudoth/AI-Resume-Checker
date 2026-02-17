from django.urls import path
from . import views

urlpatterns=[
    path('',views.display),
    path('upload/',views.upload_resume)
]