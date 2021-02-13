from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiView , name="api-view"),
    path('journalTask-detail/<str:pk>/', views.journalTaskDetail, name="task-detail"),
    path('journalTask-list/', views.journalTaskList, name="journalTask-list"),
    path('journalTask-create/', views.journalTaskCreate, name="journalTask-create"),


]




