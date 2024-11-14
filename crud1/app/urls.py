from django.urls import path

from . import views




urlpatterns = [
    path('',views.homepage,name='home'),
    path('create/',views.student_create,name='create'),
    path('details/<int:id>/',views.student_details,name='details'),
    path('update/<int:id>/',views.student_update,name='update'),
    path('delete/<int:id>/',views.student_delete,name='delete'),
]
