from django.db import models

from django_extensions.db.fields import RandomCharField


class RandomSlugModel(models.Model):
    slug = RandomCharField(length=8, lowercase=True, unique=True)

    class Meta:
        abstract = True
