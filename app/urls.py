from django.urls import path
from app import views
from .views import *
from django.contrib.auth.views import LogoutView,PasswordChangeView
urlpatterns=[
    path("",views.home.as_view(),name="home"),
    #path("add_employee/",views.EmployeeCreateView.as_view(),name="add_employee"),
    path("add_Employee/",add_Employee.as_view(),name='add_Employee'),
    path("Employee_detail/",Employee_detail.as_view(),name='Employee_detail'),
    path("submit/",views.submitrecord.as_view(),name="submit"),
    path('login/',MyLoginView.as_view(),name='login'),
    path('signup/',SignupView.as_view(),name="signup"),
    path('logout/',LogoutView.as_view(next_page='/login'),name='logout'),
    path('change-password/',PasswordChangeView.as_view(template_name='change_password.html',form_class=MyChangePasswordForm),name='change_password'),
   # path("",views.home.as_view(),name="Home"),
    
]