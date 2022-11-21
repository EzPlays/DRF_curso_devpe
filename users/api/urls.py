from django.urls import path
# from users.api.api import UserApiView
from users.api.api import user_api_view, user_detail_view

urlpatterns = [
    # path('usuarios/', UserApiView.as_view(), name='user_api')
    path('users/', user_api_view, name='user_api'),
    path('users/<int:pk>/', user_detail_view, name='user_detail_api')
]
