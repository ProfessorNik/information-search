from django.urls import path
from universities import views

urlpatterns = [
    path('', views.table),
    path('<int:pk>/', views.UniversityUpdateView.as_view()),
    path('<int:pk>/delete', views.delete),
    path('new/', views.new)
]
