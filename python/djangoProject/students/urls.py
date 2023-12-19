from django.urls import path
from . import views

urlpatterns = [
    path('', views.table),
    path('new/', views.StudentsCreateView.as_view()),
    path('<int:pk>/', views.StudentsUpdateView.as_view()),
    path('<int:pk>/delete', views.delete)
]
