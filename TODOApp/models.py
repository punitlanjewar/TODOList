from django.db import models
from django.forms import ValidationError

# Create your models here.
class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    due_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN', blank=False)

    def clean(self):
        if self.due_date and self.timestamp:
            if self.due_date < self.timestamp.date():
                raise ValidationError({'due_date': 'Due Date cannot be before Timestamp created'})
            

    def __str__(self):  # it will return the title value
        return self.title  
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):  # it will return tag names
        return self.name    
 