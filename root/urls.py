from django.urls import path
from root import views

urlpatterns = [

    path('', views.home),
    path('<slug:key>/', views.routeToUrl)

]
