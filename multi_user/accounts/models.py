from django.db import models

# Create your models here.


from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an user address')

        user = self.model(
            username=self.normalize_email(username),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        


from django.contrib.auth.models import  AbstractBaseUser,PermissionsMixin
state_choices = (
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),
    ("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry")
    )



class MyUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    
    first_name=models.CharField(max_length=100,)
    last_name=models.CharField(max_length=100,)
    email=models.EmailField(max_length=50, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)
    city=models.CharField(max_length=50, null=True, blank=True)
    pincode=models.CharField(max_length=6,null=True, blank=True)
    state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
    patient=models.BooleanField(default=False)
    doctor=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True )
    is_superuser = models.BooleanField(default=False)
  
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



