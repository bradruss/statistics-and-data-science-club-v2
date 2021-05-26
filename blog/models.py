from django.db import models
from django.utils import timezone
# from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    # Get pk as id
    id = models.PositiveIntegerField(primary_key=True)
    # text = models.TextField()
    content = models.TextField()
    post_self = models.ManyToManyField('self')
    created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
        # self.published_date = timezone.now()
        # self.save()

    def __str__(self):
        return self.title
