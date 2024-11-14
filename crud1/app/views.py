from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm




def homepage(request):
    get_data = Student.objects.all()
    context = {
        'data':get_data
    }
    return render(request,'homepage.html',context)


def student_create(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = StudentForm()
    context = {
        'form':form
    }
    return render(request,'student_create.html',context)

def student_details(request,id):
    get_student = Student.objects.get(id=id)
    context = {
        'form':get_student
    }
    return render(request,'student_details.html',context)

def student_update(request,id):
    #get a data from database
    get_student = Student.objects.get(id=id)
    #get a data from field
    form = StudentForm(instance=get_student)
    if request.method=='POST':
        #update the data
        form = StudentForm(request.POST,instance=get_student)
        form.save()
        return redirect('home')
    context = {
        'form':form
    }
    return render(request,'student_create.html',context)


def student_delete(request,id):
    student_get = Student.objects.get(id=id)
    student_get.delete()
    return redirect('home')