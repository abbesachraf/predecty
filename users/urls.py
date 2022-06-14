from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views  

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
    #re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        #views.activate, name='activate'),
    path('activate/<uidb64>/<token>/',views.activate , name='activate'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    
    
    
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
 ]
