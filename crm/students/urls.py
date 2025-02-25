from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.DashBoardView.as_view(),name='dashboard'),
    path('students-list/',views.StudentsListView.as_view(),name='students-list'),
    path('register-view/',views.StudentRegistrationView.as_view(),name='register-view'),
    # path('error-404/',views.Error404View.as_view(),name='error-404'),
    path('student-detail/<str:uuid>/',views.StudentDetailView.as_view(),name='student-detail'),
    path('student-delete/<str:uuid>/',views.StudentDeleteView.as_view(),name='student-delete'),
    path('student-update/<str:uuid>/',views.StudentUpdateView.as_view(),name='student-update'),
    
]
