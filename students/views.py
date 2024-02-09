from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from students.models import Student


# Create your views here.
@login_required(login_url="/login")

def student(request):
    return render(request, 'students.html')

@login_required(login_url="/login")
def student_add(request):
    if request.method == 'POST':
        new_student = Student.objects.create(
            name=request.POST.get('name'),
            course=request.POST.get('course'),
            date_time=request.POST.get('date_time'),
            course_date=request.POST.get('course_date'),
            room=request.POST.get('room'),
            payment=request.POST.get('payment')

        )
        new_student.save()
        return redirect('home_admin', )
    return render(request, "students_add.html")

@login_required(login_url="/login")
def student_table(request):
    mydata = Student.objects.all().values()
    template = loader.get_template('student_table.html')
    context = {
        'mymembers': mydata,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url="/login")
def set_table(request, id):
    std = Student.objects.get(id=id)
    return render(request, 'set_table.html', {'std': std})


def uprec(request, id):
    x1 = request.POST.get('name')
    x2 = request.POST.get('course')
    y1 = request.POST.get('course_date')
    x3 = request.POST.get('date_time')
    x4 = request.POST.get('room')
    x5 = request.POST.get('payment')
    std = Student.objects.get(id=id)
    std.name = x1
    std.course = x2
    std.course_date = y1
    std.date_time = x3
    std.room = x4
    std.payment = x5
    std.save()
    return redirect("/student_table")




