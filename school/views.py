from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, Teacher, Class, Student, Shedule, Grade
from .forms import SubjectForm, TeacherForm, ClassForm, StudentForm, SheduleForm, GradeForm

# Create your views here.
def index(request):
    return render(request, 'school/index.html')

def subject(request):
    subjects = Subject.objects.all()
    return render(request, 'school/subject.html', {'subject':subjects})

def del_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'school/delete_subject.html', {'subject':subjects})

def edit_subject(request, item_id):
    item = get_object_or_404(Subject, id=item_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.save()
        return redirect('subjects')
    if request.method == 'GET':
        form = SubjectForm()
        return render(request, 'school/edit_subject.html', {'form': form, 'item': item})

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher.html', {'teacher': teachers})

def clas(request):
    classes = Class.objects.all()
    return render(request, 'school/class.html', {'clas':classes})

def del_clas(request):
    classes = Class.objects.all()
    return render(request, 'school/delete_class.html', {'clas':classes})

def edit_class(request, item_id):
    item = get_object_or_404(Class, id=item_id)
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.save()
        return redirect('classes')
    if request.method == 'GET':
        form = ClassForm()
        return render(request, 'school/edit_class.html', {'form': form, 'item': item})

def student(request):
    students = Student.objects.all()
    return render(request, 'school/student.html', {'student': students})

def shedule(request):
    shedules = Shedule.objects.all()
    return render(request, 'school/shedule.html', {'shedule': shedules})

def grade(request):
    grades = Grade.objects.all()
    return render(request, 'school/grades.html', {'grade': grades})

def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
        else:
            return redirect('home')
        
    form = SubjectForm()
    context = {'form': form}
    return render(request, 'school/create_subject.html', context)

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
        else:
            return redirect('home')
        
    form = TeacherForm()
    context = {'form': form}
    return render(request, 'school/create_teacher.html', context)

def create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
        else: return redirect('home')

    form = ClassForm()
    context = {"form": form}
    return render(request, 'school/create_class.html', context)

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
        else: return redirect('home')
    form = StudentForm()
    context = {"form": form}
    return render(request, 'school/create_student.html', context)

def create_shedule(request):
    if request.method == 'POST':
        form = SheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shedule')
        else: return redirect('home')
    form = SheduleForm()
    context = {"form": form}
    return render(request, 'school/create_shedule.html', context)

def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades')
        else: return redirect('home')
    form = GradeForm()
    context = {"form": form}
    return render(request, 'school/create_grade.html', context)

def delete_subject(request, item_id):
    item = get_object_or_404(Subject, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('subjects')
    return redirect('home')

def delete_class(request, item_id):
    item = get_object_or_404(Class, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('classes')
    return redirect('home')

def show_detclass(request, item_id):
    class_instance = Class.objects.get(id=item_id)
    students = class_instance.get_students()
    return render(request, 'school/class_detail.html', {'student': students})