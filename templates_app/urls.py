from django.urls import path
from . import views

app_name = 'templates_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('profiles/', views.profile_list, name='profile_list'),
    path("contact/", views.contact, name="contact"),
    path("employee/", views.employee, name="employee"),
    path("edit_emp/<int:pk>/", views.edit_emp, name="edit_emp"),
    path("delete_emp/<int:pk>/", views.delete_emp, name="delete_emp"),
]   
