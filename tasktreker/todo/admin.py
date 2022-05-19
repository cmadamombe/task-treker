from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()
from tasktreker.todo.models import Todo


# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Task Details:', {  # The first fieldset is named “Staff personal details”
            'description': "Please capture the task details: ",
            # The first option sets the description for the group
            # 'classes': ('collapse',), #Adds the collapse class to the fieldset.
            # This will apply a JavaScript accordion style that will make the fieldset appear collapsed when
            # the form first displays
            'fields': (("title", 'description'), ("priority", "status", 'type'), 'datecompleted')
        }),

        ('Users Details:', {  # The second fieldset/group
            'description': "Please capture the client address and profile: ",
            # The  option sets the description for the group
            'classes': ('collapse',),
            # Adds the collapse class to the fieldset. This will apply a JavaScript accordion style that will make
            # the fieldset appear collapsed when the form first displays
            'fields': ("client", "assigned")
        }),
    )
    # Chooses the fields to display on the form
    list_display = ["title", 'description', "priority", "status", 'type', "datecompleted", 'client',
                    "assigned", 'created_by']
    # The fields that will be used to search the database
    search_fields = ["title", "description", 'client']
    # Field the database according to the selected fields by default
    list_filter = ('assigned',"status", 'type')
    # The results are in ascending order. To display results in descending order, use (-field_name e.g -user)
    ordering = ('-created_date',)
