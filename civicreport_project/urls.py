from django.contrib import admin
from django.urls import path, include
from reports import views as report_views # Import views to use the new functions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reports.urls')),
    path('tracking/', include('tracking.urls')),
    
    # Action URLs
    path('verify/<int:report_id>/', report_views.verify_fix, name='verify_fix'),
    path('dispute/<int:report_id>/', report_views.dispute_fix, name='dispute_fix'),
]