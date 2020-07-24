from . import views
from django.urls import path

urlpatterns = [
        path('', views.miniurl_home, name='miniurl_home'),
        path('<short>/', views.get_url, name='get_url'),
]
