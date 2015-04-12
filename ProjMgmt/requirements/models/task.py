from django.db import models
from base import ProjMgmtBase

class Task(ProjMgmtBase):
    story = models.ForeignKey('Story')    
    
    def __str__(self):
        return self.title
        
    class Meta:
        app_label = 'requirements'
        
