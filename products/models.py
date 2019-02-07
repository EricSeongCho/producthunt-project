from django.db import models
from django.contrib.auth.models import User


# Product Class
class Product(models.Model):
    # title
    title = models.CharField(max_length=255)
    # pub_date
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # url
    url = models.URLField(max_length=255, default='')
    # image
    image = models.ImageField(upload_to='images/')
    # icon
    icon = models.ImageField(upload_to='images/')
    # votes_total
    votes_total = models.IntegerField(default=1)
    # hunter
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80]

    # pub_date_pretty

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')




