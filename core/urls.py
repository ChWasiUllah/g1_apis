from django.urls import include, path
# from core.views import CustomActivationView,CustomPasswordResetConfirmView

urlpatterns = [
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    ]