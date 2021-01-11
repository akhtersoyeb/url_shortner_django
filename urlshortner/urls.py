from django.urls import path
from . import views

app_name = 'urlshortner'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<str:short_url>/', views.redirect, name='redirect'),
    path('<int:url_id>/results', views.results, name='results'),

]
