from django.db import models

# Create your models here.

class CreateLibrary(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    personal_library = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category