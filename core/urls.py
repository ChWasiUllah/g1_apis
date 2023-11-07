from django.urls import include, path
from core.views import CustomActivationView,CustomPasswordResetConfirmView

urlpatterns = [
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('activate/<str:uid>/<str:token>/', CustomActivationView.as_view(), name='activate-user'),
    path('password-reset/<str:uid>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='custom_password_reset_confirm'),
    ]