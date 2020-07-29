# urls.py
from django.urls import path


from dashboard.views import (
	UserDashboardView,
)

app_name= 'dashboard'

urlpatterns = [
    path('dashboard/', UserDashboardView.as_view(), name='userdashboardview'),
]