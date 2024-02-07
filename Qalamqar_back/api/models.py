from django.db import models

# Create your models here.


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)
    visible = models.BooleanField(max_length=250, default=False)
    image = models.CharField(max_length=250, blank=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'visible': self.visible,
            'image': self.image
        }