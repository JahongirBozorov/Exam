from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from teacher.models import Teacher


# Create your views here.

# Create your views here.
@login_required(login_url="/login")
def teacher(request):
    return render(request, 'teacher.html')


@login_required(login_url="/login")
def add_teacher(request):
    if request.method == 'POST':
        new_teacher = Teacher.objects.create(
            name=request.POST.get('name'),
            course=request.POST.get('course'),
            room=request.POST.get('room')

        )
        new_teacher.save()
        return redirect('home_admin', )
    return render(request, "add_teacher.html")


@login_required(login_url="/login")
def teacher_table(request):
    mydata = Teacher.objects.all().values()
    template = loader.get_template('teacher_table.html')
    context = {
        'tch': mydata,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url="/login")
def set_teacherTable(request, id):
    tch = Teacher.objects.get(id=id)
    return render(request, 'set_teacherTable.html', {'tch': tch})


def teacher_up(request, id):
    x1 = request.POST.get('name')
    x2 = request.POST.get('course')
    x3 = request.POST.get('room')
    tch = Teacher.objects.get(id=id)
    tch.name = x1
    tch.course = x2
    tch.room = x3
    tch.save()
    return redirect("/teacher_table")
