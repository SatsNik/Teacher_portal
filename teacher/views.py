from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'teacher/login.html', {'error': 'Invalid credentials'})
    return render(request, 'teacher/login.html')

@login_required
def home(request):
    students = Student.objects.filter(teacher=request.user)
    return render(request, 'teacher/home.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        marks = int(request.POST['marks'])
        teacher = request.user

        student = Student.objects.filter(name=name, subject=subject, teacher=teacher).first()
        if student:
            student.marks = marks
            student.save()
            messages.warning(request, "Student with same subject already exists. Marks updated.")
        else:
            Student.objects.create(name=name, subject=subject, marks=marks, teacher=teacher)
            messages.success(request, "Student added successfully!")

    return redirect('home')

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id, teacher=request.user)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.subject = request.POST['subject']
        student.marks = int(request.POST['marks'])
        student.save()
        return redirect('home')
    return render(request, 'teacher/edit_student.html', {'student': student})

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id, teacher=request.user)
    student.delete()
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'teacher/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'teacher/register.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'teacher/register.html')
