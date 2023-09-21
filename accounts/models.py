from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
from django.db.models import OneToOneField


class UserManager(BaseUserManager):
    # Aita sudhu methods carry korbe. No fields
    # Aita banabe 2 ta class
    # 1. Basic User
    # 2. Super User
    def create_user(self, first_name, last_name, username, email,
                    password=None):  # jehetu class ar under a function tai first parameter ta self e hobe
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')
        # akhon asol user banai
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)  # passwork encryption kore
        user.save(using=self._db)  # kon DB use kora hobay oita bole dawA
        return user

    # 2.Super User banano
    # Muloto amra user banaia saita k super user ar previlege dibo
    # Akhon "createUser" kora asay. tai oita call kore super user korbo
    # Super user a chaile phone number add korte parbo karon BaseUserManager babohar korsi
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    RESTAURENT = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (RESTAURENT, 'Restaurent'),
        (CUSTOMER, 'Customer')
    )
    # Aita te basic oi name email fiels name thakbe
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()  # call the model we created

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True,
                         null=True)  # Jate one user multiple account na hoye
    profile_picture = models.ImageField(upload_to='user/profile_pictures', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='user/cover_pictures', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email  # user model ar email ar sathay link
