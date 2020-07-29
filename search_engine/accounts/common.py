import os
from datetime import datetime
from PIL import Image
#creating activation codes
from random import choice, randint
from string import ascii_uppercase
from string import digits


from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse


from accounts.models import User


class SiteUrl(object):

	''' Ger secure and unsecure host name'''

	@staticmethod
	def site_url(request):
		if request.is_secure():
			site_url = 'https://'+request.get_host()
		else:
			site_url = 'http://'+request.get_host()
		return site_url


class SendMail(object):

    ''' Common Email Setting '''
    
    @staticmethod
    def mail(subject, email, email_html):
        try:
            to = [email]
            from_email = settings.EMAIL_HOST_USER
            msg = EmailMessage(subject, email_html, to=to, from_email=from_email)
            msg.content_subtype = "html"
            msg.send()
            fail_type = 1
        except:
            fail_type = 0
        return fail_type


class CreateToken:
    def __init__(self):
        pass

    new_activation_code = "".join(choice(digits) for i in range(30))

    def check_token_code_exist(self):
        try:
            code = User.objects.filter(forgot_password_token = self.new_activation_code)
        except User.DoesNotExist:
            code = None
        return code

    def generate_token_code(self):
        old_activation_code = self.check_token_code_exist()
        while old_activation_code != self.new_activation_code:
            activation_code = "".join(choice(digits) for i in range(30))
            return activation_code
        else:
            activation_code = new_activation_code
            return activation_code


class ActivationToken:
    def __init__(self):
        pass

    new_activation_code = "".join(choice(digits) for i in range(30))

    def check_token_code_exist(self):
        try:
            code = User.objects.filter(account_activate_token = self.new_activation_code)
        except User.DoesNotExist:
            code = None
        return code

    def generate_token_code(self):
        old_activation_code = self.check_token_code_exist()
        while old_activation_code != self.new_activation_code:
            activation_code = "".join(choice(digits) for i in range(30))
            return activation_code
        else:
            activation_code = new_activation_code
            return activation_code