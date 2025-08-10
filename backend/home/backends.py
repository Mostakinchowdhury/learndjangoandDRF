from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
User=get_user_model()
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        # যদি email না দেওয়া থাকে, তাহলে username কে email ধরে নাও
        if email is None:
            email = username

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
