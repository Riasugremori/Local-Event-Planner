from django.urls import path
from .views import main_view, add_event_view, event_detail

urlpatterns = [
    path('add_event/', add_event_view, name='add_event'),
    path('main/', main_view, name='main'), 
    path('events/<str:title>/', event_detail, name='event_detail'),
]
