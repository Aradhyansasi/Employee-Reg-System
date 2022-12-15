from django.urls import path
from EmployeeApp import views

urlpatterns = [
    
    path('signup',views.signup, name='signup'),
    path('home/',views.HomeView.as_view(), name='home'),
    path('',views.EmpSignInView.as_view(), name='signin'),
    path('signout', views.SignOutView, name='signout')
    

]
