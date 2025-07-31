from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Student
import csv
from django.core.paginator import Paginator

# -------------------------------------------------------------------
# Teacher Portal Views - Manages Student Data
# -------------------------------------------------------------------

@login_required
def home(request):
    """
    Display the home page with student listing.
    Supports optional search by name or subject using query parameter 'q'.
    """
    query = request.GET.get('q', '')
    students = Student.objects.filter(
        name__icontains=query
    ) | Student.objects.filter(subject__icontains=query)
    return render(request, 'home.html', {
        'students': students,
        'query': query
    })


@login_required
def add_student(request):
    """
    Handle POST request to add a student.
    - If student with same name and subject exists: adds marks to existing
    - Otherwise: creates a new student entry
    """
    if request.method == 'POST':
        name = request.POST['name'].strip()
        subject = request.POST['subject'].strip()
        try:
            marks = int(request.POST['marks'])
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'error': 'Invalid marks'})

        student, created = Student.objects.get_or_create(name=name, subject=subject)
        if not created:
            student.marks += marks
        else:
            student.marks = marks
        student.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def update_student(request):
    """
    Handle POST request to update an existing student's details.
    Fields: name, subject, marks.
    """
    if request.method == 'POST':
        student = get_object_or_404(Student, id=request.POST.get('id'))
        student.name = request.POST.get('name', '').strip()
        student.subject = request.POST.get('subject', '').strip()
        try:
            student.marks = int(request.POST['marks'])
        except (ValueError, TypeError):
            return JsonResponse({'success': False, 'error': 'Invalid marks'})

        student.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def delete_student(request, id):
    """
    Handle POST request to delete a student by ID.
    """
    if request.method == 'POST':
        Student.objects.filter(id=id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@login_required
def export_csv(request):
    """
    Export all students' data as a CSV file.
    Columns: Name, Subject, Marks
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Subject', 'Marks'])

    for s in Student.objects.all():
        writer.writerow([s.name, s.subject, s.marks])

    return response

@login_required
def home(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(
        name__icontains=query
    ) | Student.objects.filter(subject__icontains=query)

    paginator = Paginator(students, 5)  # 5 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'students': page_obj,
        'query': query,
        'page_obj': page_obj
    })