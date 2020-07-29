from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


def UserImage(instance, filename):
    file_save_path = settings.MEDIA_ROOT + \
        'user/user_{0}/{1}/{2}'.format(instance.id,
        datetime.now().strftime('%d%m%Y%H%M%S'), filename)
    file_save_pa = file_save_path.split("media/")[1]
    return file_save_pa


class BaseModel(models.Model):
    is_active = models.BooleanField(default = False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        abstract=True 


class User(AbstractUser):

    ''' User model for extra info '''
    user_pic = models.ImageField(upload_to = UserImage, null = True, blank = False)
    email = models.CharField(unique = True, max_length = 200, null = False, blank = False)
    account_activate_token = models.CharField(max_length = 200, null = False, blank = False)
    forgot_password_token = models.CharField(max_length = 200, null = False, blank = False)
    
    def __str__(self):
       return self.email



class EmailTemplate(BaseModel):
    title = models.CharField(max_length=255, default='', blank=True, null=True)
    subject = models.CharField(max_length=255, default='', blank=True, null=True)
    content = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return str(self.title)