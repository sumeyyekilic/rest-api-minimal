from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiView , name="api-view"),
    path('task-detail/<str:pk>/', views.journalTaskDetail, name="task-detail"),
]




