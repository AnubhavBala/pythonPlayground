from django.shortcuts import render
from projects.models import Project

def project_idx(request):
	projects = Project.objects.all()
	context = {
		'projects': projects
	}
	return render(request,'project_idx.html',context)

def project_dtl(request,pk):
	project = Project.objects.get(pk=pk)
	context = {
	'project': project
	}
	return render(request,'project_dtl.html',context)


# Create your views here.
