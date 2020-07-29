from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailOrUsernameBackendAuth(ModelBackend):
    """
    custom backend to authenticated user by phone number or his username
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_name = str(username)
        if '@' in user_name:
            try:
                user = UserModel.objects.get(email=user_name)
                
                pwd_valid = user.check_password(password)
                if pwd_valid:
                    return user
                return None
            except UserModel.DoesNotExist:
                return None
        else:
            try:
                user = UserModel.objects.get(username=user_name)
                pwd_valid = user.check_password(password)
                if pwd_valid:
                    return user
                return None
            except UserModel.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
