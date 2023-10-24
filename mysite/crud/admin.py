from django.contrib import admin
from crud.models import myinfo

class myinfoadmin(admin.ModelAdmin):
    list_display=('fname','lname','id_no','ideas')


admin.site.register(myinfo,myinfoadmin)

# Register your models here.
