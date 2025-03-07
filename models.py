from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom manager for creating users
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class StaffUserManager(BaseUserManager):
    def create_user(self, staff_id, password=None, role=None):
        if not staff_id:
            raise ValueError('Staff ID is required')
        user = self.model(staff_id=staff_id, role=role)
        user.set_password(password)  # This hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, staff_id, password=None):
        user = self.create_user(staff_id, password, role='admin')
        user.is_admin = True
        user.is_superuser = True  # Mark as superuser
        user.save(using=self._db)
        return user

class StaffUsers(AbstractBaseUser):
    ROLE_CHOICES = [
        ('shopkeeper', 'Shopkeeper'),
        ('admin', 'Admin'),
        ('principal', 'Principal'),
        ('mess-incharge', 'Mess-Incharge'),
        ('gm','GM'),
        ('accountant','Accountant')
    ]

    staff_id = models.CharField(max_length=10, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')
    email = models.EmailField(null=True, blank=True, unique=True)  # Allow NULL values
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expiration = models.DateTimeField(null=True, blank=True)

    objects = StaffUserManager()

    USERNAME_FIELD = 'staff_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.staff_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Material(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Purchased quantity (optional)
    used_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Used quantity
    available_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Non-editable, managed by views.py
    unit = models.CharField(max_length=50, null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    entry_time = models.DateTimeField(default=timezone.now)
   
    def __str__(self):
        return f"{self.name} on {self.date}"
    
class Purchase(models.Model):
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=255, unique=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50,null=True,blank=True)
    is_acknowledged = models.BooleanField(default=False)
    is_printed = models.BooleanField(default=False)
    reference_id = models.CharField(max_length=100,null=True,blank=True)
    is_fetched = models.BooleanField(default=False) 

class Need(models.Model):
     date = models.DateField(default=timezone.now)
     No_of_persons=models.PositiveIntegerField(default=0)
     name = models.CharField(max_length=100)
     quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
     unit = models.CharField(max_length=50,null=True,blank=True)
     is_acknowledged = models.BooleanField(default=False)
     is_printed = models.BooleanField(default=False)
     is_fetched = models.BooleanField(default=False)  # New field to track fetched status
     reference_id = models.CharField(max_length=100,null=True,blank=True)
     def __str__(self):
        return f"{self.material_name} - {self.quantity} units"


from decimal import Decimal
class Received(models.Model):
    
    name = models.CharField(max_length=100)  # Name of the material
    received_date = models.DateField()
    unit = models.CharField(max_length=50, null=True, blank=True)
    received_quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_received = models.BooleanField(default=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")
    is_fetched = models.BooleanField(default=False)  # New field to track fetched status


    def save(self, *args, **kwargs):
        # Automatically determine the status and update is_received
        if self.received_quantity is None or self.received_quantity == Decimal(0):
            self.status = "Pending" if self.received_quantity is None else "Not Received"
            self.is_received = False
        elif self.received_quantity > Decimal(0):
            self.status = "Received"
            self.is_received = True
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Received {self.received_quantity} units of {self.name} on {self.received_date}"


class Mess_menu_Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    year = models.CharField(max_length=9)  # e.g., '2024-2025'
    breakfast = models.TextField()
    lunch = models.TextField()
    snacks = models.TextField()
    dinner = models.TextField()

    def __str__(self):
        return f"{self.day} ({self.year})"
    
    from django.db import models

class Item(models.Model):
    """Model representing an item in the grocery list."""
    name = models.CharField(max_length=100, unique=True)  # Ensures unique item names

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['id']  # Orders by 'id' in ascending order





