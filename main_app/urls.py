from django.urls import include, path
from . import views

urlpatterns =[
    path('api/v1/create_call', views.CallCreate.as_view()),
    path('api/v1/create_client', views.ClientCreate.as_view()),
    path('api/v1/update_client/<int:pk>', views.ClientCreate.as_view()),
  #  path('api/v1/get_medic/<int:pk>', views.MedicsRetrieve.as_view()),
]