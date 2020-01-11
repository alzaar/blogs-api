from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=1200)
  pub_date = models.DateTimeField(auto_now=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title