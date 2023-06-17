from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    wecrec_employee = models.BooleanField(default = False)
    pass

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class UserCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    

    class Meta:
        unique_together = ('user', 'company') 

class PaymentOptions(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Proyect(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100 ,null=True)
    description = models.TextField( null=True)
    address = models.TextField( null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Expenses(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    payment_option = models.ForeignKey(PaymentOptions, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE, null=True, blank=True)
    bill = models.ForeignKey("Bill", on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class Bill(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bill_image = models.ImageField(upload_to='bills/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)