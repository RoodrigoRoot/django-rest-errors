from django.db import models
from django.shortcuts import reverse
# Create your models here.


class CategoryError(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("error:error-category", kwargs={'name': self.name})

    class Meta:
        ordering = ["-name"]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Error(models.Model):

    error_code = models.CharField(max_length=80, unique=True)
    message = models.CharField(max_length=250)
    category = models.ForeignKey(CategoryError, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.error_code

    def get_absolut_url(self):
        return reverse("error:error-code", kwargs={'error_code': self.error_code})

    class Meta:
        ordering = ["-error_code"]
        verbose_name = 'Error'
        verbose_name_plural = 'Errors'

