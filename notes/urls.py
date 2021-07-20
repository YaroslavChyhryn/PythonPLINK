from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "note"

router = DefaultRouter()
router.register(r'note', views.NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]
