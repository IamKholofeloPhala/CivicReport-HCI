from django.shortcuts import render, redirect, get_object_or_404
from .models import Report

def index(request):
    if request.method == "POST":
        category = request.POST.get('category')
        location = request.POST.get('location')
        description = request.POST.get('description')
        
        # This saves the new report to the database
        Report.objects.create(
            category=category, 
            location=location, 
            description=description,
            status='Pending'
        )
        return redirect('dashboard')
        
    return render(request, 'reports/index.html')

def verify_fix(request, report_id):
    # This finds the specific report or shows a clean 404 if not found
    report = get_object_or_404(Report, id=report_id)
    report.status = 'Resolved' 
    report.save()
    return redirect('dashboard')

def dispute_fix(request, report_id):
    # This addresses the "False Resolution" complaint from the reviews
    report = get_object_or_404(Report, id=report_id)
    report.status = 'Disputed' 
    report.save()
    return redirect('dashboard')