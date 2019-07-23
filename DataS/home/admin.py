from django.contrib import admin

# Register your models here.
from .models import HotTables
from .models import Tables,TableDetails

admin.site.register(HotTables)
admin.site.register(Tables)
admin.site.register(TableDetails)
