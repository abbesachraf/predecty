from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('profile/', views.profile, name='profile'),
    path("home.html",views.result),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('home.html?result', views.result, name = 'home.html?result'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('data', views.dashboard_with_pivot, name='data'),
    path('test', views.test , name='test'),
]
