from django.db import models
from authors import models as authors_models
# Create your models here.
class Comments(models.Model):
    text = models.TextField()
    author = models.ForeignKey(authors_models.Authors, models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'