from django.urls import path
# from .views import get_users, create_user

# urlpatterns = [
#     path('users/', get_users, name='get_users'),
#     path('users/create-user', create_user, name='create_user'),
# ]

# api/urls.py

from .views import get_users, create_user, create_user_view

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create-user/', create_user_view, name='create_user_view'),  # Atualize aqui
]
