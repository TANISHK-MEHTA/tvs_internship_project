from import_export import resources
from .models import TestCases

class TestCasesResource(resources.ModelResource):
    class Meta:
        model = TestCases