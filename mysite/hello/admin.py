from django.contrib import admin

from .models import Person


# Register your models here.


class ShowAllAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]


class PersonAdmin(ShowAllAdmin):
    list_display = ()


admin.site.register(Person, PersonAdmin)
