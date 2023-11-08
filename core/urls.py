from django.views.generic import TemplateView
from django.urls import include, path
# from core.views import CustomActivationView,CustomPasswordResetConfirmView

urlpatterns = [
    path('',TemplateView.as_view(template_name = 'account/index.html')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    ]