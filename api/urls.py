from django.urls import path
from .views import LoginView, ProfileView, APIUsageView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('api-usage/', APIUsageView.as_view()),
]
