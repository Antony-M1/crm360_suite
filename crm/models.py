from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _gl
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete
from django.dispatch import receiver
# Create your models here.

class UserAU(AbstractUser):

    USERNAME_FIELD = 'username'
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        db_table = "tabUser"
        verbose_name = 'User'
        

class Salutation(models.Model):
    
    salutation = models.CharField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return self.salutation

    class Meta:
        db_table = "tabSalutation"
        verbose_name = 'Salutation'
        


class Gender(models.Model):
    
    gender = models.CharField(
        db_column='gender', 
        max_length=255,
        unique=True,
        db_comment='Person Gender',
        help_text= 'Gender of the Person.',
        verbose_name='Person Gender'
        )
    
    def __str__(self) -> str:
        return self.gender
    
    class Meta:
        db_table = "tabGender"
        verbose_name = 'Gender'


class LeadSource(models.Model):
    
    source_name = models.CharField(
        db_column='source_name',
        max_length=255,
        unique=True,
        verbose_name= 'Source Name',
        help_text='To mention the which platform we get this source'
    )
    details = models.TextField(
        db_column='details',
        blank=True,
        null=True,
        verbose_name='Source Details',
        help_text='Mention more details about the source'
    )
    
    def __str__(self) -> str:
        return self.source_name
    
    class Meta:
        db_table = "tabLead Source"
        verbose_name = "Lead Source"


class Customer(models.Model):

    CUSTOMER_TYPE = [
        ('Company', "Company"),
        ('Individual', "Individual"),
    ]
    
    salutation = models.ForeignKey(
                    "Salutation",
                    on_delete=models.CASCADE,
                )
    customer_name = models.CharField(
        max_length=255,
        verbose_name='Customer Name',
        help_text='Mention the customer name it may individual or company name'
    )
    customer_type = models.CharField(
        max_length=50,
        choices=CUSTOMER_TYPE,
        default='Company',
        verbose_name='Customer Type',
        help_text='It may be a individual or'
    )
    
    class Meta:
        db_table = "tabCustomer"
        verbose_name = "Customer"


class Territory(models.Model):
    
    name = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True,
        db_column='name',
        verbose_name='Teritory Name',
        help_text='Name of the Teritory'
    )
    parent_name = models.ForeignKey(
        'Territory',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    
    def clean(self):
        '''
            This method triggers before save the model
        '''
        if self.name == self.parent_name:
            raise ValidationError(f'the name - {self.name} and the parent name - {self.parent_name} should not same')
    
    class Meta:
        db_table = "tabTerritory"
        verbose_name = "Teritory or Region"

@receiver(pre_delete, sender=Territory)
def territory_pre_delete(sender, instance, **kwargs):
    # Custom code to run before the instance is deleted
    print(f"Deleting {instance.name} (ID: {instance.parent_name})")