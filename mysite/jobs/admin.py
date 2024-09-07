from django.contrib import admin

from .models import Job, candidate


# Register your models here.
class cunstomAdmin(admin.ModelAdmin):
    list_display = ('JobName','WorkPlace','WorkKind','JobID')

class candidateAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','job_wanted')

admin.site.register(Job,cunstomAdmin)

admin.site.register(candidate,candidateAdmin)
