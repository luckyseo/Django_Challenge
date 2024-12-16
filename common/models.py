from django.db import models


# Create your models here.
class CommonModel(models.Model):
    """
    Common model Definition
    """

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        # Django won't save to DB
