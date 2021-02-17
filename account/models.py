from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an Email.")
        if not username:
            raise ValueError("User must have an Username.")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=256, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    full_name = models.CharField(max_length=256, default="Rahber Abbas")

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class VendorAccount(models.Model):
    org_name = models.CharField(max_length=256)
    per_name = models.CharField(max_length=256)
    org_email = models.EmailField(max_length=256, unique=True)
    org_phone = models.IntegerField()
    add1 = models.CharField(max_length=1000)
    add2 = models.CharField(max_length=1000)
    state = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    pincode = models.CharField(max_length=256)
    lat = models.CharField(max_length=256, default="12231")
    lon = models.CharField(max_length=256, default="12123")
    value = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, default=Account, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.org_name

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=256)
    ven_name = models.CharField(max_length=256)
    ven_email = models.EmailField(unique=True, max_length=256)
    ven_phone = models.IntegerField()
    add = models.TextField()
    state = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    pincode = models.IntegerField()
    lat = models.DecimalField(max_digits=40, null=True, blank=True, decimal_places=10)
    lon = models.DecimalField(max_digits=40, null=True, blank=True, decimal_places=10)
    value = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.org_name

@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Account)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
