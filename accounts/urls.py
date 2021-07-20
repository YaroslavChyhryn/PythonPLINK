from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('token', views.UserToken.as_view(), name='token'),
    path('requests', views.RequestsFromCurrentIP.as_view(), name='requests'),
]

