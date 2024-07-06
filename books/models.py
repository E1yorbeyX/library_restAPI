from django.db import models

# Create your models here.
class Books(models.Model):
      class Meta:
            verbose_name = 'Book'
            verbose_name_plural = 'Books'
        
      title = models.CharField(max_length=200)
      author = models.CharField(max_length=200)
      description = models.TextField(max_length=1000)
      isbn = models.CharField(max_length=13)
      price = models.DecimalField(max_digits=20, decimal_places=2)

      def __str__(self):
            return self.title
      
