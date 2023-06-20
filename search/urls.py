from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('quintuple/', views.quintuple, name='quintuple'),
    path('<slug:doc_name>/', views.detail, name='detail')

]
