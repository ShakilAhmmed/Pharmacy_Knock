import os, sys, random, django

# Django Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pharmacy_management_src.settings')
django.setup()

from faker import Faker
from backend_main.models import PatientModel


def populate_patient(n):
    faker_data = Faker()
    for _ in range(n):
        patient_model = PatientModel()
        patient_model.patient_name = faker_data.name()
        patient_model.patient_phone = faker_data.phone_number()
        patient_model.patient_alternative_phone = faker_data.phone_number()
        patient_model.patient_email = faker_data.email()
        patient_model.patient_address = faker_data.address()
        patient_model.patient_status = random.choice(['Active', 'Inactive'])
        patient_model.save()
    print("Data Populated Successfully")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please Put Action")
    else:
        try:
            n = int(sys.argv[2])
        except IndexError:
            n = 10
        if sys.argv[1] == 'populate_patient':
            populate_patient(n)
