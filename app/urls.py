from django.urls import path
from .views import resume_views

urlpatterns = [
    path('', resume_views, name='resume_views'),
]