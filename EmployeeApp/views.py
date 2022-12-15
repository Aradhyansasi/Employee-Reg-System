from django.shortcuts import render,redirect
from .models import User
from EmployeeApp.forms import RegistrationForm, LoginForm
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def signup(request):
    if request.method == 'POST':
        f = RegistrationForm(request.POST)

        if f.is_valid():
            u = f.save(commit=False)
            raw_password = User.objects.make_random_password(length=10, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz01234567889")
            u.set_password(raw_password)
            u.save()

            print("password is: ", raw_password)
            subject = 'Login password'
            message = f'Welcom {u.emp_name}, your password is {raw_password}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [u.email ]
            send_mail( subject, message, email_from, recipient_list )
            
            messages.success(request, "Registration successful." )
            return redirect("signin")

        else:
            messages.error(request,'Invalid credentials')

    else:
        f = RegistrationForm()

    context ={"form":f}
    return render(request, 'Emp_reg.html', context)


# def signup(request):

#     f = RegistrationForm(request.POST)
#     if f.is_valid():
#         u = f.save(commit=False)
#         raw_password = User.objects.make_random_password(length=10, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz01234567889")
#         u.set_password(raw_password)
#         u.save()

#         print("password is: ", raw_password)
#         subject = 'Login password'
#         message = f'Welcom {u.emp_name}, your password is {raw_password}.'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [u.email ]
#         send_mail( subject, message, email_from, recipient_list )

#         messages.success(request, "Registration successful." )
#         return redirect("signin")
#     return render(request, 'Emp_reg.html', context={"form":f})


class HomeView(TemplateView):
    template_name='empHome.html'



class EmpSignInView(FormView):
    model = User
    form_class = LoginForm
    template_name = 'EmpLogin.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print("******* email:",email)
            print("******* password:",password)
            user = authenticate(request, email=email, password=password)
            print("******* user:",user)
            if not user:
                return render(request, 'EmpLogin.html', {'form':form})
            login(request,user)
            return redirect('home')


def SignOutView(request, *args, **kwargs):
    logout(request)
    return redirect('signin')