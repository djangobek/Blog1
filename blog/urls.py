from django.urls import path
from .views import hello_world, home, about, service, contact


urlpatterns = [
    path('', hello_world, name='hello'),
    path('home/', home, name='home_page'),
    path('about/', about, name='about_page'),
    path('service/', service, name='service_page'),
    path('contact/', contact, name='contact_page')
]
