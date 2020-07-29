from django.urls import path


from accounts.views import (
	HomeView,
	SignupView,
	LoginView,
	LogoutView,
	ForgotPasswordView,
	ResetPasswordView
)

app_name= 'accounts'

urlpatterns = [
    path('', HomeView.as_view(), name='homeview'),
    path('singup/', SignupView.as_view(), name='singupview'),
    path('login/', LoginView.as_view(), name='loginview'),
    path('logout/', LogoutView.as_view(), name='logutview'),
    path('forgot/password/', ForgotPasswordView.as_view(), name='forgotpasswordview'),
    path('reset/password/', ResetPasswordView.as_view(), name='resetpasswordview'),
]