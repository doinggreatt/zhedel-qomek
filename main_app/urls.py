from django.urls import include, path
from . import views

urlpatterns =[
    path('api/v1/create_call', views.CallCreate.as_view()), # POST за создания вызова создать вызов
 
    path('api/v1/update_working_status/<int:pk>', views.CarsUpdate.as_view()), # UPDATE запрос который отправляется водителем когда заходит на службу

    path('api/v1/set_arrived/<int:id>', views.SetCallArrived.as_view()), # UPDATE запрос который говорит о том что водитель прибыл на вызов
    
    path('api/v1/get_call_status/<int:id>', views.CallCreate.as_view()), # GET запрос который спамится со стороны юзера

    path('api/v1/update_car_geo/<int:id>', views.CarGeoUpdate.as_view()) # UPDATE запрос который спамится со стороны водителя и говорит о том где находится машина

    
]