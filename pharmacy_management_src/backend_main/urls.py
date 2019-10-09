from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(BackendView.as_view()), name="backend-home"),
    path('add_patient', add_patient, name="add_patient"),
    path('patient_list', patient_list, name="patient_list"),
    path('patient_list/status/<int:pk>', patient_status, name="patient_status"),
    path('patient_list/delete/<int:pk>', patient_delete, name="patient_delete"),
    path('patient_list/edit/<int:pk>', patient_edit, name="patient_edit"),
    path('medicine', medicine, name="medicine"),
    path('medicine_list', medicine_list, name="medicine_list"),
    path('medicine_sell_view/<int:pk>', medicine_sell_view, name="medicine_sell_view"),
    path('medicine_sell_delete/<int:pk>', medicine_sell_delete, name="medicine_sell_delete"),
    path('medicine_sell_edit/<int:pk>', medicine_sell_edit, name="medicine_sell_edit"),
    path('setup', setup, name="setup"),
    path('profile', profile, name="profile"),

]
