from django.urls import path
from . import views

urlpatterns = [
    path('sahifa1/', views.page1, name='sahifa1'),
    path('sahifa2/', views.page2, name='sahifa2'),
    path('sahifa3/', views.page3, name='sahifa3'),
    path('sahifa4/', views.page4, name='sahifa4'),
    path('sahifa5/', views.page5, name='sahifa5'),
]