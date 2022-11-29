from django.db import models

class Projects(models.Model):

    projects_id=models.IntegerField(primary_key=True,max_length=10)

    projects_description=models.TextField()

    projects_title=models.CharField(max_length=50)

    projects_creator=models.CharField(max_length=50)



class Issues(models.Model):

    issues_id=models.IntegerField(primary_key=True,max_length=10)

    issues_type=models.CharField(max_length=20)

    issues_title=models.CharField(max_length=50)

    issues_description=models.TextField()

    issues_reporter=models.CharField(max_length=50)

    issues_assignee=models.CharField(max_length=50)

    issues_status=models.CharField(max_length=20)

    issue_project_title=models.ForeignKey(Projects, on_delete=models.CASCADE)



# Create your models here.
