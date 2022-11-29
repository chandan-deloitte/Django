from rest_framework import generics

from .models import Projects, Issues
from .serializers import ProjectSerializer, IssuesSerializer

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()
    # def get_queryset(self):
    #     queryset = Projects.objects.all()
    #     projects_title = self.request.queryparams.get('projects_title')
    #     if projects_title is not None:
    #         queryset = queryset.filter(issue_project_title=projects_title)
    #     return queryset

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()

class IssuesList(generics.ListCreateAPIView):
    serializer_class = IssuesSerializer
    queryset = Issues.objects.all()

class IssuesDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IssuesSerializer
    queryset = Issues.objects.all()
