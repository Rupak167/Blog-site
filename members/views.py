from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm,EditProfileForm,PasswordChange
# Create your views here.


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChange
    #form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('login')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user