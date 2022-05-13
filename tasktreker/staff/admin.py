from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
from tasktreker.staff.models import Staff


# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Staff Personal Details:', {  # The first fieldset is named “Staff personal details”
            'description': "Please capture the staff personal details: ",
            # The first option sets the description for the group
            # 'classes': ('collapse',), #Adds the collapse class to the fieldset.
            # This will apply a JavaScript accordion style that will make the fieldset appear collapsed when
            # the form first displays
            'fields': (("user", 'gender', "title"), ("date_of_birth", "staff_phone"), "company_name")
        }),

        ('Physical Address & Profile Summary:', {  # The second fieldset/group
            'description': "Please capture the staff address and profile: ",
            # The  option sets the description for the group
            'classes': ('collapse',),
            # Adds the collapse class to the fieldset. This will apply a JavaScript accordion style that will make
            # the fieldset appear collapsed when the form first displays
            'fields': ("address", "staff_profile_summary")
        }),
    )
    # Chooses the fields to display on the form
    list_display = ["user", 'title', "staff_phone", "date_of_birth", "gender", 'company_name',
                    "created_date", "modified_date"]
    # The fields that will be used to search the database
    search_fields = ["user", "staff_phone", 'company_name']
    # Field the database according to the selected fields by default
    list_filter = ('gender',)
    # The results are in ascending order. To display results in descending order, use (-field_name e.g -user)
    ordering = ('user',)
