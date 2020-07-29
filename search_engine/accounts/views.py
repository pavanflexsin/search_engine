from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views.generic.edit import FormView
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q


from accounts.forms import (
	SignUpForm,
	UserAuthenticationForm
)
from accounts.common import (
    CreateToken, 
    SendMail,
    ActivationToken
)
from accounts.models import User


class HomeView(TemplateView):
    template_name = "website_layout/home.html"


class SignupView(CreateView):
    model = User 
    form_class = SignUpForm
    template_name = 'website_layout/signup.html'

    def get_success_url(self):
        obj = ActivationToken()
        activtion_token = obj.generate_token_code()
        email_html = "Your new password is : " + activtion_token
        '''' -----Email Settings----- '''
        objemail = SendMail.mail("Activation Link", self.object.email, email_html )
        '''' -----End Email setting----- '''
        if objemail:
            self.object.account_activate_token = activtion_token
            self.object.is_ative = False
            self.object.save()
            messages.success(self.request, 'We have sent acount activation to your registered email address.Please click on link and activate your account.')
        else:
            messages.success(self.request, 'Email did not send.Please try again letter.')
            # self.object.delete()
        return reverse('accounts:singupview')


class LoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = "website_layout/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return redirect(reverse_lazy('dashboard:userdashboardview'))
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return super().get_success_url()


class LogoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        """
        Logout user and redirect to target url.
        """
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class ForgotPasswordView(TemplateView):
    template_name = "website_layout/forgot_password.html"

    def post(self, request, *args, **kwargs):
        adminforgot = User.objects.filter(Q(email = request.POST['username']) | Q(username = request.POST['username']), is_superuser = False)
        if adminforgot:
            obj = CreateToken()
            forgot_password_tkn = obj.generate_token_code()
            email_html = "Your new password is : " + forgot_password_tkn
            '''' -----Email Settings----- '''
            objemail = SendMail.mail("Activation Link", adminforgot[0].email, email_html )
            '''' -----End Email setting----- '''
            if objemail:
                adminforgot[0].forgot_password_token = forgot_password_tkn
                adminforgot[0].save()
                messages.add_message(request, messages.SUCCESS, "Activation link send to your registered email address.")
                return redirect('accounts:forgotpasswordview')
            else:
                messages.add_message(request, messages.ERROR, "Email did not send to your registered email address.Please try again letter.")
                return redirect('accounts:forgotpasswordview')
        else:
            messages.add_message(request, messages.ERROR,"Username/Email does not exist.")
            return redirect('accounts:forgotpasswordview')


class ResetPasswordView(TemplateView):
    models = User
    template_name = "website_layout/reset_password.html"
    # def get(self, request):
    #     adminforgot = User.objects.filter(forgot_password_token = '')
    #     if adminforgot:
    #         pass
    #     else:
    #         messages.add_message(request, messages.ERROR,"Invalid link.")
    #         return redirect('accounts:forgotpasswordview')