from django.urls import path

from SortAlgorithm.algorithm_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sort/', views.sort_array, name='sort_array'),

]