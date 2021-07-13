from django.db import models

class Blog(models.Model): 
    title=models.CharField(max_length=200) #제한O
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField() #제한X
    body=models.TextField()

    def __str__(self):
        return self.title
