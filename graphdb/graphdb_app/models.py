from django.db import models

class GraphDB(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    blazegraph_url = models.URLField()
    blazegraph_user = models.CharField(max_length=255)
    blazegraph_password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
