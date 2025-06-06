from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_teacher, name='register_teacher'),
    path('home/', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('logout/', views.logout_view, name='logout'),
]
