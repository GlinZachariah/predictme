from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(MSFT)
admin.site.register(CSCO)
admin.site.register(Twitter_MSFT)
admin.site.register(Twitter_CSCO)
admin.site.register(PredictData_MSFT)
admin.site.register(PredictData_CSCO)