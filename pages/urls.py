from django.urls import path
from .views import HomePageView, LoginPageView, AboutPageView  

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('about/', AboutPageView.as_view(), name='about'),
]