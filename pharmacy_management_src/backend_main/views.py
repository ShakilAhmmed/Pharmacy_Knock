from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import View

from .forms import PatientForm, MedicineSellForm, SetupForm, SignUpForm
from django.contrib import messages
from .models import PatientModel, MedicineSellModel, SellDetialsModel, SetUpModel
from django.core.paginator import Paginator
import os
from django.contrib.auth import update_session_auth_hash


# Create your views here.
class BackendView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'backend/home.html')


@login_required
def profile(request):
    template_name = "backend/User/profile.html"
    users = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=users)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "User Profile Updated Successfully")
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = SignUpForm(instance=users)
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def setup(request):
    template_name = "backend/Setup/setup.html"
    setup_data = SetUpModel.objects.first()
    old_file = setup_data.company_logo
    image = setup_data.company_logo.url if setup_data.company_logo else ''
    if request.method == "POST":
        form = SetupForm(request.POST, request.FILES, instance=setup_data)
        if form.is_valid():
            if request.FILES:
                new_file = request.FILES.get('company_logo')
                if not old_file == new_file:
                    if os.path.isfile(old_file.path):
                        os.remove(old_file.path)
            form.save()
            messages.success(request, 'Setup Updated Successfully')
            return HttpResponseRedirect(reverse('setup'))
    else:
        form = SetupForm(instance=setup_data)
    context = {
        'form': form,
        'image': image
    }
    return render(request, template_name, context)


@login_required(login_url='/')
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Patient Added Successfully')
            return HttpResponseRedirect(reverse('add_patient'))
    else:
        form = PatientForm()
    context = {
        'form': form
    }
    return render(request, 'backend/Patient/patient.html', context)


@login_required(login_url='/')
def patient_list(request):
    patient_list = PatientModel.objects.filter(is_deleted=False).order_by('-created_at')
    if request.GET.get('request_for_search') == "request_for_search":
        filter = True
        if request.GET.get('patient_name'):
            patient_name = request.GET.get('patient_name').strip()
            print(patient_name)
            patient_list = patient_list.filter(patient_name__icontains=patient_name)
        if request.GET.get('patient_phone'):
            patient_phone = request.GET.get('patient_phone').strip()
            patient_list = patient_list.filter(patient_phone__icontains=patient_phone)
        if request.GET.get('patient_status'):
            patient_list = patient_list.filter(patient_status=request.GET.get('patient_status'))
    else:
        paginator = Paginator(patient_list, 25)
        page = request.GET.get('page')
        patient_list = paginator.get_page(page)
        filter = False
    context = {
        'patient_list': patient_list,
        'filter': filter
    }
    return render(request, 'backend/Patient/patient_list.html', context)


@login_required(login_url='/')
def patient_status(request, pk):
    patient_data = get_object_or_404(PatientModel, pk=pk)
    if patient_data.patient_status == 'Active':
        patient_data.patient_status = 'Inactive'
        messages.info(request, 'Patient Status Changed Into Inactive')
    else:
        patient_data.patient_status = 'Active'
        messages.success(request, 'Patient Status Changed Into Active')
    patient_data.save()
    return HttpResponseRedirect(reverse('patient_list'))


@login_required(login_url='/')
def patient_delete(request, pk):
    data = get_object_or_404(PatientModel, pk=pk)
    data.soft_delete()
    messages.warning(request, 'Patient Data Deleted Successfully')
    return HttpResponseRedirect(reverse('patient_list'))


@login_required(login_url='/')
def patient_edit(request, pk):
    data = get_object_or_404(PatientModel, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient Updated Successfully')
            return HttpResponseRedirect(reverse('patient_edit', kwargs={'pk': pk}))
    else:
        form = PatientForm(instance=data)
    context = {
        'form': form
    }
    return render(request, 'backend/Patient/patient_edit.html', context)


def Enquiry(lis1):
    if lis1[0] == '':
        return False


@login_required(login_url='/')
def medicine(request):
    if request.method == 'POST':
        medicine_name = request.POST.getlist('medicine_name[]')
        total_course = request.POST.getlist('total_course[]')
        total_buy = request.POST.getlist('total_buy[]')
        medicine_form = MedicineSellForm(request.POST)
        if medicine_form.is_valid():
            medicine_pk = medicine_form.save(commit=False)

            if Enquiry(medicine_name) == False and Enquiry(total_course) == False and Enquiry(total_buy) == False:
                medicine_pk.save()
                for i in range(len(medicine_name)):
                    sell_details = SellDetialsModel();
                    sell_details.medicine_sell_id = medicine_pk
                    sell_details.medicine_name = medicine_name[i]
                    sell_details.total_course = total_course[i]
                    sell_details.total_buy = total_buy[i]
                    sell_details.save()

                messages.success(request, "Medicine Sell Details Save Successfully")
            else:
                messages.error(request, "Medicine Sell Details Fill Up Correctly")

                return HttpResponseRedirect(reverse(medicine))
    else:
        medicine_form = MedicineSellForm()
    context = {
        'form': medicine_form
    }
    return render(request, 'backend/Medicine/medicine.html', context)


@login_required
def medicine_list(request):
    medicine_sell = MedicineSellModel.objects.filter(is_deleted=False).order_by('-created_at')
    context = {
        'medicine_sell': medicine_sell
    }
    return render(request, 'backend/Medicine/medicine_list.html', context)


@login_required
def medicine_sell_delete(request, pk):
    delete_sell = get_object_or_404(MedicineSellModel, pk=pk).delete()
    delete_medicine_sell = SellDetialsModel.objects.filter(medicine_sell_id=pk).delete()
    messages.success(request, "Medicine Sell Details Delete Successfully")
    return HttpResponseRedirect(reverse('medicine_list'))


@login_required
def medicine_sell_edit(request, pk):
    medicine_coustomer = get_object_or_404(MedicineSellModel, pk=pk)
    sell_data = SellDetialsModel.objects.select_related().filter(medicine_sell_id=pk).order_by('-created_at')
    if request.method == "POST":
        medicine_name = request.POST.getlist('medicine_name[]')
        total_course = request.POST.getlist('total_course[]')
        total_buy = request.POST.getlist('total_buy[]')
        medicine_form = MedicineSellForm(request.POST, instance=medicine_coustomer)
        if medicine_form.is_valid():
            sell_pk = medicine_form.save(commit=False)

            if Enquiry(medicine_name) == False and Enquiry(total_course) == False and Enquiry(total_buy) == False:
                delete_medicine_sell = SellDetialsModel.objects.filter(medicine_sell_id=sell_pk).delete()
                sell_pk.save()
                for i in range(len(medicine_name)):
                    sell_details = SellDetialsModel();
                    sell_details.medicine_sell_id = sell_pk
                    sell_details.medicine_name = medicine_name[i]
                    sell_details.total_course = total_course[i]
                    sell_details.total_buy = total_buy[i]
                    sell_details.save()
                messages.success(request, "Medicine Sell Details Updated Successfully")
            else:

                messages.error(request, "Medicine Sell Details Fill Up Correctly")
                return HttpResponseRedirect(reverse('medicine_sell_edit', kwargs={'pk': pk}))


    else:
        medicine_form = MedicineSellForm(instance=medicine_coustomer)
    context = {
        'form': medicine_form,
        'details_sell': sell_data
    }
    return render(request, 'backend/Medicine/medicine_edit.html', context)


@login_required
def medicine_sell_view(request, pk):
    medicine_coustomer = get_object_or_404(MedicineSellModel, pk=pk)
    sell_data = SellDetialsModel.objects.select_related('medicine_sell_id').filter(medicine_sell_id=pk).order_by(
        '-created_at')
    context = {
        'sell_data': sell_data,
        'medicine_coustomer': medicine_coustomer
    }

    return render(request, 'backend/Medicine/medicine_sell_view.html', context)


@login_required(login_url='/')
def notify(request):
    if request.method == "POST":
        return HttpResponse("POST")
    else:
        return render(request, 'backend/Medicne')
