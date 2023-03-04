from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.base import TemplateView
from .models import EmployeeManagement
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login
from .forms import *
from django.contrib import messages
from .models import EmployeeManagement

# Create your views here.

########### HomePage ##############
class home(TemplateView):
    template_name='app/home.html'

###### Employee details page #################
class EmployeeCreateView(CreateView):
    model=EmployeeManagement
    fields=['First_name','last_name','EmailId','Mobile','Address','Blood_Group']
    success_url='/submit/'

class submitrecord(TemplateView):
    template_name='app/submit.html'

##############################################
class MyLoginView(View):
    def get(self,request):
        fm=myloginform()
        return render(request,"login.html",{'form':fm})
    def post(self,request):
        fm=myloginform(request,data=request.POST)    
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,'login.html',{'form':fm})

class SignupView(View):
    def post(self,request):
        fm=signupform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Signup Success!")
            return redirect('/signup')
        else:
            return render(request,'signup.html',{'form':fm})     
    def get(self,request):
        fm=signupform()
        return render(request,'signup.html',{'form':fm}) 
       
class add_Employee(View):
    def get(self,request):
        fm=Addemployeeform()
        return render(request,'add_Employee.html',{'form':fm})    

    def post(self,request):
        fm=Addemployeeform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Added Successfully!")
            return redirect('/add_Employee')
        else:
            return render(request,'add_Employee.html',{'form':fm})        
class Employee_detail(View):
    def get(self,request):
        employee_data=EmployeeManagement.objects.all()
        employee=len(employee_data)
        return render(request,'Employee_detail.html',{'Employee_data':employee_data,'Employee':employee})
