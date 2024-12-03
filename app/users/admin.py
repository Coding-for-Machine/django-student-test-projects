from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    list_display = ['email','book_icon']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()
    # icon
    def book_icon(self, obj):
        return format_html('<i class="fa-solid fa-user-graduate"></i>')  # Iconni qo‘shish
    book_icon.short_description = 'Foydalanuvchilar-Icon'

admin.site.register(User, UserAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['created_at','bio', 'profile_icon']
    # icon 
    def profile_icon(self, obj):
        return format_html('<i class="fa-regular fa-address-card"></i>')  # Iconni qo‘shish
    profile_icon.short_description = 'Profile-Icon'
admin.site.register(Profile, ProfileAdmin)