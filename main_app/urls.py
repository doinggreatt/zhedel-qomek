from django.urls import include, path
from . import views

urlpatterns =[
    path('api/create_call', views.CallsCreate.as_view()),
    path('api/create_client', views.ClientsCreate.as_view()),
    path('api/get_medic/<int:pk>', views.MedicsRetrieve.as_view()),
]