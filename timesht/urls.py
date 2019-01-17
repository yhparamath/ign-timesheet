from django.urls import path
from . import views

urlpatterns = [
	path('',views.get_name, name = 'index'),
	path('login/', views.login, name="login"),
	path('thanks/', views.thank_you, name="thanks"),
]