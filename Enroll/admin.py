from django.contrib import admin
from Enroll import models
# Register your models here.
class templeAdmin(admin.ModelAdmin):
    list_display = ('name','Monk','Details','latitude','Longitude',)


admin.site.register(models.category)
admin.site.register(models.temple, templeAdmin)