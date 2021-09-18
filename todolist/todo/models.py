from django.db import models
 
class todoData(models.Model):
    title=models.CharField(max_length=500,null=True)
    status=models.BooleanField(default=False)
    creation=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
