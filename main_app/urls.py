from django.urls import include, path
from . import views

urlpatterns =[
    path('api/v1/create_call', views.CallCreate.as_view()),
    path('api/v1/create_client', views.ClientCreate.as_view()), # POST, creating clients
    path('api/v1/update_client/<int:pk>', views.ClientCreate.as_view()),
    path('api/v1/call_accepted/<int:pk>', views.CallCreate.as_view()),
    path('api/v1/update_working_status/<int:pk>', views.CarsUpdate.as_view()),
    path('api/v1/update_car_geo/<int:pk>', views.CarGeoUpdate.as_view()),
    path('api/v1/set_arrived/<int:id>', views.SetCallArrived.as_view()), 
    path('api/v1/get_call_status/<int:id>', views.CallCreate.as_view())
]