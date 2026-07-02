from django.db import models

"""
Data models for Product, Category and Tag
Relationship:
    - Product -> Category: One to Many (One Category can have multiple Prodcuts)
    - Prodcut <-> Tags: Many to Many (A Product can have multiple Tags and 
                        a Tag can have multiple Products)
"""
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )
    tags = models.ManyToManyField(
        Tag, 
        related_name="products"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name