from account.forms import UserCreationForm,UserChangeForm
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User, Otp,Address,Message








class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["phone","fullname","email", "is_admin", 'show_image']
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["fullname", "image"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "fullname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code')
    search_fields = ('phone',)


# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('__str__','fullname', 'sub')


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# admin.site.register(Otp)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(Address)
admin.site.register(Message)
