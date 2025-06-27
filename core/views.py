from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import SemesterResult
from .forms import SemesterForm, SubjectFormSet

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def get_feedback(score):
    if score >= 3.75:
        return "Excellent! Keep up the great work! 🎉"
    elif score >= 3.0:
        return "Good job! You can do even better! 💪"
    elif score >= 2.0:
        return "Needs improvement. Stay focused and seek help if needed. 📚"
    else:
        return "At risk! Please consult your advisor immediately! 🚨"

@login_required
def dashboard(request):
    semesters = SemesterResult.objects.filter(user=request.user).order_by('-created_at')
    
    total_points = sum(s.gpa * s.total_credits for s in semesters)
    total_credits = sum(s.total_credits for s in semesters)
    cgpa = round(total_points / total_credits, 2) if total_credits > 0 else 0.0
    
    latest_gpa = semesters[0].gpa if semesters else 0.0
    gpa_feedback = get_feedback(latest_gpa)
    cgpa_feedback = get_feedback(cgpa)

    return render(request, 'core/dashboard.html', {
        'semesters': semesters,
        'cgpa': cgpa,
        'gpa_feedback': gpa_feedback,
        'cgpa_feedback': cgpa_feedback,
    })

@login_required
@transaction.atomic
def add_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            semester = form.save(commit=False)
            semester.user = request.user
            semester.save()

            formset = SubjectFormSet(request.POST, instance=semester)
            if formset.is_valid():
                formset.save()
                semester.calculate_gpa()
                return redirect('dashboard')
    else:
        form = SemesterForm()
        formset = SubjectFormSet()

    return render(request, 'core/add_semester.html', {
        'form': form,
        'formset': formset,
    })

@login_required
@transaction.atomic
def edit_semester(request, semester_id):
    semester = get_object_or_404(SemesterResult, id=semester_id, user=request.user)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        formset = SubjectFormSet(request.POST, instance=semester)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            semester.calculate_gpa()
            return redirect('dashboard')
    else:
        form = SemesterForm(instance=semester)
        formset = SubjectFormSet(instance=semester)

    return render(request, 'core/edit_semester.html', {
        'form': form,
        'formset': formset,
        'semester': semester,
    })

@login_required
def delete_semester(request, semester_id):
    semester = get_object_or_404(SemesterResult, id=semester_id, user=request.user)
    if request.method == 'POST':
        semester.delete()
        return redirect('dashboard')
    return render(request, 'core/delete_semester.html', {'semester': semester})
