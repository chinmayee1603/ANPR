from django.contrib import admin

# Register your models here.
from .models import Cardata, Bankdetails, chalan

admin.site.register(Cardata)
admin.site.register(Bankdetails)
admin.site.register(chalan)
