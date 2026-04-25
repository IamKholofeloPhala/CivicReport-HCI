from django.shortcuts import render
from reports.models import Report

def dashboard(request):
    # Fetch all reports from the database, newest first
    all_reports = Report.objects.all().order_by('-created_at')
    return render(request, 'tracking/dashboard.html', {'reports': all_reports})