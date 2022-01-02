from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView 
from .forms import SignUpForm,EditProfileForm,PasswordChange,ProfilePageForm,EditProfilePageform
from blog.models import Profile,Post
# Create your views here.

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class =EditProfilePageform
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    #fields = ['bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url','linkedin_url']


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    #fields= '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self , *args , **kwargs ):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self ).get_context_data(*args , **kwargs)

        page_user = get_object_or_404(Profile, id= self.kwargs['pk'])
        user_posts = Post.objects.filter(id = self.kwargs['pk'])
        context["page_user"] = page_user
        context["user_posts"] = user_posts
        return context


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