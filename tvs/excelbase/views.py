from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TestCases, TestCaseInstance, Project
from .resources import TestCasesResource
from tablib import Dataset
from datetime import datetime
from django.db.models import Count 
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        'projects': projects,
    }
    return render(request, 'excelbase/home.html', context)

@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.owner = request.user
            project.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'excelbase/project_form.html', context)

@login_required(login_url='login')
def project(request, pk):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    project = get_object_or_404(Project, pk=pk, owner=request.user)  # Get the specific project

    if q == '':
        instances = project.test_case_instances.all()
    else:
        q = datetime.strptime(q, '%B %d, %Y').date()
        print(q)
        
        instances = project.test_case_instances.filter(created=q)
        print(instances)
        print(instances[0])
        if instances.count() == 0:
            return redirect('home')

    datesLeft = project.test_case_instances.order_by('created').values('created').distinct()

    context = {
        'project': project,
        'instances': instances,
        'datesLeft': datesLeft,
    }
    
    if request.method == 'POST':
        ts = TestCasesResource()
        dataset = Dataset()
        excel_file = request.FILES['excel_file']
        data_import = dataset.load(excel_file.read(), format='xlsx')
        # result = ts.import_data(data_import, dry_run=True)  # Test the data import
        # if not result.has_errors():
        #     ts.import_data(data_import, dry_run=False)
        instance = TestCaseInstance.objects.create(project=project)
        for i in range(len(data_import)):
            value = TestCases(
                root=instance,
                testCase=data_import[i][1],
                result=data_import[i][2],
                reason=data_import[i][3],
            )
            value.save()
            
    return render(request, 'excelbase/project.html', context)

@login_required(login_url='login')
def getTestCaseByInstance(request):
    instance_id = request.GET.get('instance_id')
    instance = get_object_or_404(TestCaseInstance, pk=instance_id) # pk = primary key
    testcases = instance.test_cases.all()

    frequencies = instance.test_cases.all().values('result').annotate(Count('result'))

    context = {
        'instance': instance,
        'testcases': testcases,
        'frequencies': frequencies,
    }
    return render(request, 'excelbase/testCase.html', context)
