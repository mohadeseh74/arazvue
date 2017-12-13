from django.contrib import admin
from service.models import OurService , ServiceDetail




class ServiceDetailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(OurService)
admin.site.register(ServiceDetail, ServiceDetailAdmin)
