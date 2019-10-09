from django.db import models

# Create your models here.
from django.utils import timezone


class PatientModel(models.Model):
    patient_name = models.CharField(max_length=150)
    patient_phone = models.CharField(max_length=20, unique=True)
    patient_alternative_phone = models.CharField(max_length=20)
    patient_email = models.EmailField(max_length=50, blank=True)
    patient_address = models.TextField()
    patient_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.patient_name


class MedicineSellModel(models.Model):
    coustomer_name = models.ForeignKey(PatientModel, on_delete=models.DO_NOTHING, default=1)
    coustomer_contact = models.CharField(max_length=20)
    medicine_buy_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


class SellDetialsModel(models.Model):
    medicine_sell_id = models.ForeignKey(MedicineSellModel, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=50)
    total_course = models.CharField(max_length=100)
    total_buy = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


class SetUpModel(models.Model):
    company_title = models.CharField(max_length=100)
    company_address = models.TextField()
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=14)
    company_logo = models.ImageField(upload_to='setup/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
