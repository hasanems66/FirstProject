from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.models import User, Address,Message
from django.core import validators



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('phone',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        # fields = ["phone", "fullname","password", "is_active", "is_admin"]
        fields = ["phone", "fullname","email","image"]




# def start_with_0(value):
#     if value[0] != '0':
#         raise forms.ValidationError('Phone Should Start With 0')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'شماره موبایل خود را وارد کنید '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'پسورد خود را وارد کنید'}))


    def clean_phone(self):
        username = self.cleaned_data.get('username')
        if len(username) > 30:
            raise ValidationError('Invalid value: %(value)s is invalid should be 11 characters',
                                  code='invalid',
                                  params={'value': f'{username}'}
                                  )


    # def clean(self):
    #     cd=super().clean()
    #     phone =cd['phone']
    #     if len(phone) > 11:
    #         raise ValidationError('Invalid value: %(value)s is invalid',
    #                               code='invalid',
    #                               params={'value': f'{phone}'}
    #                               )
    #     return phone


class OtpLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder':'شماره موبایل خود را وارد کنید '}), validators=[validators.MaxLengthValidator(11)])




class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'کد تایید جهاررقمی را وارد کنید '}),
                           validators=[validators.MaxLengthValidator(4)]
                           )



class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)
    class Meta:
        model = Address
        fields = '__all__'
        # exclude = ('user',)


class MessageForm(forms.ModelForm):
    class Meta:
        model= Message
        fields= '__all__'


