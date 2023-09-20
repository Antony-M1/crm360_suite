from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# Create your models here.


class User(AbstractBaseUser):

    abstract_base_user = models.CharField(
        max_length=255
    )
    sslc_mark = models.IntegerField(verbose_name='SSLC Mark Verbose Name')
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    
    class Meta:
        db_table = "users"

class UserAU(AbstractUser):
        
    abstract_user = models.CharField(max_length=255)
    hsc_mark = models.IntegerField(verbose_name='HSC Mark Verbose Name')

    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        db_table = "tabUser"