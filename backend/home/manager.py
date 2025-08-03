from django.contrib.auth.base_user import BaseUserManager

class myUserManager(BaseUserManager):
    def create_user(self,username,email,phone_num,password=None,**extra_field):
        if not email:
            raise ValueError("Email is a requred field")
        if not phone_num:
            raise ValueError("phone number is a requred field")
        email=self.normalize_email(email)
        user=self.model(email=email,password=password,phone_num=phone_num,username=username,**extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,phone_num,password=None,**extra_field):
        extra_field.setdefault("is_superuser",True)
        extra_field.setdefault("is_staff",True)
        extra_field.setdefault("is_active",True)
        return self.create_user(username,email,phone_num,password,**extra_field)

    def active_user(self):
        return self.get_queryset().filter(is_active=True)
