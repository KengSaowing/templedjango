from django.contrib import admin
from Enroll import models
# Register your models here.
class templeAdmin(admin.ModelAdmin):
    list_display = ('id_temple','name','Monk','Details','latitude','Longitude',)


admin.site.register(models.Category)
admin.site.register(models.temple, templeAdmin)