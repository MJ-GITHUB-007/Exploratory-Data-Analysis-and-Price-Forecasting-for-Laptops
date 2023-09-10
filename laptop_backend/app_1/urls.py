from django.urls import path
from app_1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predictor/', views.predictor, name='predictor'),
    path('result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    path('contact_email/', views.contact_email, name='contact_email'),
    path('contact_whatsapp/', views.contact_whatsapp, name='contact_whatsapp'),
    path('contact_other_options/', views.contact_other_options, name='contact_other_options')
]
