import uuid

from django.db import models


class Publisher(models.Model):
    """
    Book Publisher model
    Managed only in admin
    """
    COUNTRIES = {
        "US": "United States",
        "FR": "France",
        "GB": "Great Britain",
    }
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2, choices=COUNTRIES, help_text="2-letter Country Code", default=COUNTRIES["US"])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} fom {self.country}"
