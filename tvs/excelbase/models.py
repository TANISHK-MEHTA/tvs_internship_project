from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='projects')

    class Meta:
        ordering = ['-created'] # newest first

    def __str__(self):
        return self.name

class TestCaseInstance(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='test_case_instances')
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created'] # newest first

    def __str__(self):
        return f"Test Case Instance {self.id}"

class TestCases(models.Model):
    root = models.ForeignKey(TestCaseInstance, on_delete=models.CASCADE, null=True, related_name='test_cases')
    testCase = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    reason = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.testCase