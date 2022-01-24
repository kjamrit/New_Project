from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='polls-home' ),
    path('greeting/',views.greeting, name='polls-greeting'),
    path('about/',views.about, name='polls-about')
]