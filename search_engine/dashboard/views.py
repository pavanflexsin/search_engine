from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin



from accounts.models import User


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "user_dashboard/dashboard.html"