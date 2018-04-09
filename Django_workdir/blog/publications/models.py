from django.db import models
from django.urls import reverse
from authors import models as authors_models
from categories import models as categories_models
# Create your models here.

class Publications(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    author = models.ForeignKey(authors_models.Authors, on_delete=models.CASCADE)
    category = models.ManyToManyField(categories_models.Categories, related_name='pub')
    content = models.TextField()
    image = models.ImageField(upload_to='pub_images')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('post-details', args=[self.slug])