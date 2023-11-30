from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login', views.UserLogin.as_view(), name='user_login'),
    # path('register', views.RegisterView.as_view(), name='user_register'),
    path('otplogin', views.OtpLoginView.as_view(), name='otp_login'),
    path('checkotp', views.CheckOtpView.as_view(), name='check_otp'),
    path('logout', views.user_logout, name= 'user_logout'),
    path('add/address', views.AddAddressView.as_view(), name='add_address'),
    path('contact/us', views.contact_us, name='contact_us'),
    path('edit', views.UserEditView.as_view(), name='user_edit'),
    # path('edit', views.user_edit, name='user_edit'),
]