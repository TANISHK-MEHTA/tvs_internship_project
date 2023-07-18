from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project/<str:pk>', views.project, name="project"),
    path('create_project/', views.createProject, name="create_project"),
    path('instance/', views.getTestCaseByInstance, name='instance'),
]
