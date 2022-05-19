from django.db import models

# Create your models here.
class BlogContent(models.Model):
    title = models.CharField(max_length=100, default = "")
    timestamp = models.DateField(auto_now_add=True)
    head1 = models.CharField(max_length=100, default="")
    body1 = models.CharField(max_length=500, default="")
    head2 = models.CharField(max_length=100, default="")
    body2 = models.CharField(max_length=500, default="")
    head3 = models.CharField(max_length=100, default="")
    body3 = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="blog/images", default="")


    def __str__(self):
        return self.title
