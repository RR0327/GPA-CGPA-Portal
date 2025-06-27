from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('add-semester/', views.add_semester, name='add_semester'),
    path('edit-semester/<int:semester_id>/', views.edit_semester, name='edit_semester'),
    path('delete-semester/<int:semester_id>/', views.delete_semester, name='delete_semester'),
]
