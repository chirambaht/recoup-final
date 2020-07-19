from django.contrib import admin
from .models import Athelete, Practice, KB, plan
# Register your models here.
admin.site.register(plan)
admin.site.register(Athelete)
admin.site.register(Practice)
admin.site.register(KB)
