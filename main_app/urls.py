from django.urls import include, path
from . import views

urlpatterns =[
    path('api/v1/create_call', views.CallCreate.as_view()),
 
    path('api/v1/update_working_status/<int:pk>', views.CarsUpdate.as_view()),

    path('api/v1/set_arrived/<int:id>', views.SetCallArrived.as_view()),
    
    path('api/v1/get_call_status/<int:id>', views.CallCreate.as_view()), # get for check car's geolocation

    path('api/v1/update_car_geo/<int:id>', views.CarGeoUpdate.as_view()) # id - call_id

    
]