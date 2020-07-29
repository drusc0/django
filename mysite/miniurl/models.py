from django.db import models

STATUS = (
    (0, "Inactive"),
    (1, "Active")
)


# we will create the necessary model for tiny url system
class Miniurl(models.Model):
    original_url = models.CharField(max_length=512, unique=True)
    short_url = models.CharField(max_length=64, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"
