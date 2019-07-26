from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    name = models.CharField(max_length=264, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, related_name='webpage')
    url = models.URLField(unique=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("myapp:detail", kwargs={"pk": self.pk})

    def get_success_url(self):
        return reverse_lazy('myapp:detail')

class AcessRecord(models.Model):
    date = models.DateField()
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
