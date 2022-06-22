from django.db import models


class AllFiles(models.Model):
    name_file = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    file_urls = models.CharField(max_length=300)

    def __str__(self):
        return self.name_file