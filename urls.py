from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
]
