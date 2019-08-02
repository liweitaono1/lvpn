from django.db import models


# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey()
    modify = models.ForeignKey()
    create_time = models.DateTimeField(auto_created=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    def __unicode__(self):
        return self.id
