from django.urls import path

from .import views


urlpatterns = [

     path('browse/<str:region>/<str:category>/', views.browse, name='browse'),
     path('details/<str:name>', views.details, name='details'),
     path('', views.index, name='index'),
     path('api/', views.api, name='api'),
     path('weather/', views.weather, name='api'),

    ]

