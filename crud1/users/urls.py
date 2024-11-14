from django.urls import path
from . import views




urlpatterns = [
    path('signup/',views.signup_page,name='signup'),
    path('signin/',views.signin_page,name='signin'),
    path('logout/',views.user_logout,name='logout'),
]
