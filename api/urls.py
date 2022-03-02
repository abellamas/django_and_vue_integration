from django.urls import path
from .views import AlumnosView

urlpatterns = [
    path('alumnos/',AlumnosView.as_view(), name="alumnos"),
    path('alumnos/<int:dni>/',AlumnosView.as_view(), name="alumnos_id"),
]
