from django.contrib import admin
from .models import Slots, Days, Calendar
# Register your models here.

admin.site.register(Slots)
admin.site.register(Days)
admin.site.register(Calendar)