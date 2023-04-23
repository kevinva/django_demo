from django.urls import path
from . import views


app_name = 'demo'
urlpatterns = [
    path('index/', views.index, name='index'),

    path('create/', views.create_test, name='create_test'),

    path('create_bulk/', views.craete_bulk_test, name='create_bulk_test'),

    path('delete/<int:aid>/', views.delete_by_id, name='delete_by_id'),

    path('deletev2/', views.delete_by_title, name='delete_by_title'),

    path('update/', views.update_test, name='update_test'),

    path('query/', views.query_test, name='query_test'),
]