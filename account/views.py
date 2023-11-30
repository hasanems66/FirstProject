from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse
from django.shortcuts import render
from django.views import View
from .forms import LoginForm, OtpLoginForm, CheckOtpForm, AddressCreationForm,UserChangeForm
from .models import User, Otp, Message
from django.utils.crypto import get_random_string
from uuid import uuid4

import ghasedakpack
from random import randint

SMS = ghasedakpack.Ghasedak('f5e0deb95b0a29088a59c07ae31f9efe8b09669f7c4b2ab8c7c67c083b98bbbf')


# def user_login(request):
#     return render(request, 'account/login.html', context={})

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:main')
            else:
                form.add_error('username', 'There is no user with this number')
                form.add_error('password', 'The Password Is Incorrect')

        else:
            form.add_error('username', 'The information entered is not correct')

        return render(request, 'account/login.html', context={'form': form})


class OtpLoginView(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, 'account/otplogin.html', context={'form': form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            SMS.verification({'receptor': cd["phone"], 'type': '1', 'template': 'randcode', 'param1': randcode})
            # token = get_random_string(length=100) # 1
            token = str(uuid4())  # 2
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            # return redirect(reverse('account:check_otp') + f'?phone={cd["phone"]}') # send phone withe url to checkotp 1
            return redirect(reverse('account:check_otp') + f'?token={token}')  # send token withe url to checkotp 2
        else:
            form.add_error('phone', 'The information entered is not correct')

        return render(request, 'account/otplogin.html', context={'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/check_otp.html', context={'form': form})

    def post(self, request):
        # phone = request.GET.get('phone')  # get phone from url form register
        token = request.GET.get('token')  # get token from url form register
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect('account:user_edit')

        else:
            form.add_error('phone', 'The information entered is not correct')

        return render(request, 'account/check_otp.html', context={'form': form})


class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
        next_page = request.GET.get('next')
        if next_page:
            return redirect(next_page)

        return render(request, 'account/add_address.html', context={'form': form})

    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'account/add_address.html', context={'form': form})


class UserEditView(View):
    def get(self, request):
        user = request.user
        form = UserChangeForm(instance=user)
        return render(request, 'account/user_edit.html', context={'form': form})

    def post(self, request):
        form = UserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home:main')
        return render(request, 'account/user_edit.html', context={'form': form})

#
# def user_edit(request):
#     user = request.user
#     form = UserEditForm(instance=user)
#     if request.method == 'POST':
#         form = UserEditForm(data=request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#
#     return render(request, 'account/user_edit.html', context={'form': form})


def contact_us(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        body = request.POST.get('body')
        Message.objects.create(full_name=full_name, email=email, sub=sub, body=body)

    return render(request, 'account/contact_us.html', context={})


def user_logout(request):
    logout(request)
    return redirect('home:main')
