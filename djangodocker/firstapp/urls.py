from django.urls import path
from .views import ProjectList, ProjectDetails,IssuesList,IssuesDetails

urlpatterns = [
    path('projects/',ProjectList.as_view()),
    path('projects/<int:pk>/',ProjectDetails.as_view()),
    path('issues/',IssuesList.as_view()),
    path('issues/<int:pk>/',IssuesDetails.as_view()),
]