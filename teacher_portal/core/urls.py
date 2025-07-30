from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/', views.update_student, name='update_student'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
]