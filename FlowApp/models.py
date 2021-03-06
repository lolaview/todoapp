from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    Done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
