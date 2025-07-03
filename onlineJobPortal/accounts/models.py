from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_admin(self, company_name, company_address, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email           = self.normalize_email(email),
            username        = username,
            first_name      = first_name,
            last_name       = last_name,
            company_name    = company_name,
            company_address = company_address,
        )
        user.is_admin      = True
        user.is_active     = True
        user.is_staff      = False
        user.is_superadmin = False

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email      = self.normalize_email(email),
            username   = username,
            first_name = first_name,
            last_name  = last_name,
        )
        user.is_admin      = False
        user.is_active     = True
        user.is_staff      = True
        user.is_superadmin = False

        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email      = self.normalize_email(email),
            username   = username,
            password   = password,
            first_name = first_name,
            last_name  = last_name,
        )
        user.is_admin      = True
        user.is_active     = True
        user.is_staff      = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)
    
    company_name    = models.CharField(max_length=300, blank=True, null=True)
    company_address = models.TextField( blank=True, null=True)
    
    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class UserProfile(models.Model):
    Gender =(
        ('no','Select'),
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    user              = models.OneToOneField(Account, on_delete=models.CASCADE)
    profession_title  = models.CharField(max_length=50, blank=True,  null=True)
    date_of_birth     = models.DateField(blank=True,  null=True)
    current_address   = models.CharField(blank=True, max_length=100,  null=True)
    permanent_address = models.CharField(blank=True, max_length=100,  null=True)
    profile_picture   = models.ImageField(blank=True, upload_to='userprofile',  null=True)
    gender            = models.CharField(choices=Gender, max_length=20, default='no',  null=True, blank=True)

    def __str__(self):
        return self.user.first_name

class EducationQualification(models.Model):
    user                  = models.ForeignKey(Account, on_delete=models.CASCADE)
    education_degree      = models.CharField(max_length=100,blank=True, null=True)
    education_board       = models.CharField(max_length=100,blank=True, null=True)
    education_institution = models.CharField(max_length=100,blank=True, null=True)
    graduation_year_from  = models.DateField(blank=True, null=True)
    graduation_year_to    = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.user.first_name
    
class OtherInfo(models.Model):
    user          = models.ForeignKey(Account, on_delete=models.CASCADE)
    major_skill   = models.CharField(max_length=150, blank=True, null=True)
    facebook_url  = models.CharField(max_length=150, blank=True, null=True)
    instagram_url = models.CharField(max_length=150, blank=True, null=True)
    linkedin_url  = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.user.first_name