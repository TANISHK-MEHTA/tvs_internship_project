from django.contrib import admin
from .models import TestCases, TestCaseInstance
# Register your models here.
admin.site.register(TestCaseInstance)
admin.site.register(TestCases)
