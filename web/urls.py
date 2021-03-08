from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('listen', views.listen, name='listen'),
    path('prem', views.prem, name='prem'),
    path('prodospecs', views.prodospecs, name='prodospecs'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),

]
