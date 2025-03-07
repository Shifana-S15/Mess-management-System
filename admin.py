# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import StaffUsers

# class StaffUserAdmin(BaseUserAdmin):
#     list_display = ('staff_id', 'role', 'is_admin')  # Correct fields here
#     search_fields = ('staff_id',)  # Correct fields here
#     ordering = ('staff_id',)  # Ensure this refers to an existing field

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

# admin.site.register(StaffUsers, StaffUserAdmin)


from django.contrib import admin
#from .models import Room, Student, Staff, Booking, Faculty
import django.apps
class mess_admin(admin.AdminSite):
    site_header='mess'
admin_site=mess_admin(name='mess_admin')

models=django.apps.apps.get_models()
for model in models:
    try:
        admin_site.register(model)
    except:
        print("model not found")