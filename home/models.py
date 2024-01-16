from django.db import models
from django.contrib.auth.models import User

class CommentM(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    like = models.BooleanField(default=True)


    def __str__(self):
        return f'{ self.author} - {self.body}'



class CreatelikeM(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.Model)
    status = models.BooleanField(default=True)
    comment = models.ForeignKey(to=CommentM, on_delete=models.CASCADE)

    def __str__(self):
        return self.author









