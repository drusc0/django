from . import views
from django.urls import path

urlpatterns = [
        path('<short>/', views.get_url, name='get_url'),
]
