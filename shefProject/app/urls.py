from django.urls import path
from app.views import Home

urlpatterns=[



    path('', Home.as_view(), name='Home')


]