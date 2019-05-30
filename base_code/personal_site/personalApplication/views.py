# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, redirect  
from personalApplication.forms import EmployeeForm  
from personalApplication.models import Employee
from django.contrib.auth.decorators import login_required
from personalApplication.functions import handle_uploaded_file  
from personalApplication.forms import StudentForm
from django.http import HttpResponse 
# Create your views here.  

@login_required
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm() 
    return render(request,'index.html',{'form':form})

@login_required(login_url='/login/')  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})

@login_required  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})

@login_required  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})
    
@login_required  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

@login_required
def upload(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"upload.html",{'form':student})
