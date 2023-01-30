from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=500)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[0:300]

    def pub_date_preety(self):
        return self.pub_date.strftime('%b'+'/'+'%e'+'/'+'%Y')

