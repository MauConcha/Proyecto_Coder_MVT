from App1.views import mostrar_familiares
from django.urls import path

urlpatterns = [
    path('', mostrar_familiares),
]