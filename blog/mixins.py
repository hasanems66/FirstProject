from django.shortcuts import redirect



class CustomLoginRequireMixin:
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('account:otp_login')
        else:
            return super(CustomLoginRequireMixin, self).dispatch(request,*args,**kwargs)