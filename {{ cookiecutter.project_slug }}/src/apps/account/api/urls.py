"""
URLs de las View de Django REST Framework aplicación `src.apps.account`

"""
from django.urls import path

from src.apps.account.api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
]
