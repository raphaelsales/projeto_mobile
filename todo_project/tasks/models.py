from django.db import models

# Create your models here.
class Task(models.Model):
    CATEGORY_CHOICES = [
        ('P', 'Pessoal'),
        ('PR', 'Profissional'),
        ('A', 'Acadêmico'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
