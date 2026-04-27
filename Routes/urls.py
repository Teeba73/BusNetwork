from django.urls import path
from . import views

app_name = 'Routes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:route_id>', views.route_details, name='Route_details'),
    path('<int:route_id>/book/', views.book, name='Book'),
    path('<int:route_id>/unbook/', views.unbook, name='Unbook'),
    path('station/<int:station_id>/', views.station_detail, name='Station_details')
]