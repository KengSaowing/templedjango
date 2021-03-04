from django.contrib import admin
from Enroll import models
# Register your models here.
class templeAdmin(admin.ModelAdmin):
    list_display = ('name','Monk','Details','Detailsa','Detailsb','latitude','Longitude',)

    search_fields =('name',)


admin.site.register(models.Category)
admin.site.register(models.temple, templeAdmin)