from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
# Create your views here.
# class LoginView(View):
#     template_name="login_panel/login.html"
#     def get(self,*args, **kwargs):
#         return render(self.request,self.template_name)
#     def post(self,request,*args, **kwargs):
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Log In Successfully')
#             return HttpResponseRedirect(reverse("backend-home"))
#         else:
#             messages.warning(request, 'Your User Not Valid')
#             return HttpResponseRedirect(reverse("login"))
@login_required
def userlogout(request):
        logout(request)
        messages.info(request, 'Logged Out Successfully')
        return HttpResponseRedirect(reverse('login'))
