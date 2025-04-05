from django.db import models
import uuid

class Data(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.id)} ----- {self.created_at.hour}:{self.created_at.minute}:{self.created_at.second}'