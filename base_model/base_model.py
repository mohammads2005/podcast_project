from abc import abstractmethod

from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Date Updated")
    description = models.TextField(verbose_name="Description")
    is_allowed = models.BooleanField(default=False, verbose_name="Allowed Activities")

    class Meta:
        abstract = True
        ordering = ("pk",)

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError("Please Implement the (__str__) method")
