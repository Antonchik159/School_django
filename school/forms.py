from .models import Subject, Teacher, Class, Student, Shedule, Grade
from django.forms import ModelForm, TextInput, Select, DateTimeInput, NumberInput

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть назву предмета'
            })
        }

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "surname", "subject"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть ім’я викладача'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть прізвище викладача'
            }),
            "subject": Select(attrs={
                'class': 'form-control',
                'placeholder':'Введіть предмет який веде викладач'
            })
        }

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть клас/группу'
            })
        }

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surename", "class_group"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть імя студента'
            }),
            "surename": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Введіть Прізвище студента'
            }),
            "class_group": Select(attrs={
                'class': 'form-control',
                'placeholder':'клас/группа'
            })
        }

class SheduleForm(ModelForm):
    class Meta:
        model = Shedule
        fields = ["date_time", "teacher", "subject", "class_group"]
        widgets = {
            "date_time": DateTimeInput(attrs={
                'placeholder': 'Введіть дату і час',
                'type': 'datetime-local'
            }),
            "teacher": Select(attrs={
                'class': 'form-control'
            }),
            "subject": Select(attrs={
                'class': 'form-control'
            }),
            "class_group": Select(attrs={
                'class': 'form-control'
            })
        }

class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = ["grade", "student", "subject"]
        widget = {
            "grade": NumberInput(attrs={
                'placeholder': 'Оцінка студента',
                'class': 'form-control'
            }),
            "student": Select(attrs={
                'class': 'form-control'
            }),
            "subject": Select(attrs={
                'class': 'form-control'
            })
        }