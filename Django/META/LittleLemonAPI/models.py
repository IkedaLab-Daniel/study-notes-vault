"""Models for the Little Lemon API app."""

from django.db import models

class Category(models.Model):
    """Model representing a menu category."""
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.title)

class MenuItem(models.Model):
    """Model representing a menu item."""
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.title)
