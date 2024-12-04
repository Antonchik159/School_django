from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва предмету")

    def __str__(self) -> str:
        return f"{self.name}"
    
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я викладача")
    surname = models.CharField(max_length=100, verbose_name="Прізвище викладача")
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, verbose_name="Предмет який викладає")

    def __str__(self) -> str:
        return f"{self.surname}, {self.name}"
    
class Class(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва класу")

    def __str__(self) -> str:
        return f"{self.name}"
    
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я студента")
    surename = models.CharField(max_length=100, verbose_name="Прізвище студента")
    class_group = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.name}, {self.surename}"
    
class Shedule(models.Model):
    date_time = models.DateTimeField(verbose_name="Дата та час проведення")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=1)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    class_group = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.date_time} - {self.subject} ({self.class_group})"
    
class Grade(models.Model):
    grade = models.PositiveIntegerField(verbose_name="Оцінка")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.student} - {self.subject}: {self.grade}"